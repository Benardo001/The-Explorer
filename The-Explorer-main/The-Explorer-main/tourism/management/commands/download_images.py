import os
import json
import requests

from django.core.management.base import BaseCommand
from django.apps import apps
from django.conf import settings


class Command(BaseCommand):
    help = 'Download images and attach to model instances. Provide a JSON mapping file.'

    def add_arguments(self, parser):
        parser.add_argument('mapping_file', type=str, help='Path to a JSON file with array of {"model":"ModelName","id":1,"url":"https://..."}')

    def handle(self, *args, **options):
        mapping_file = options['mapping_file']
        if not os.path.exists(mapping_file):
            self.stderr.write(f'Mapping file not found: {mapping_file}')
            return

        with open(mapping_file, 'r', encoding='utf-8') as fh:
            items = json.load(fh)

        for item in items:
            model_name = item.get('model')
            pk = item.get('id')
            url = item.get('url')
            if not model_name or not pk or not url:
                self.stderr.write(f'Skipping invalid entry: {item}')
                continue

            Model = apps.get_model('tourism', model_name)
            if Model is None:
                self.stderr.write(f'Model not found: {model_name}')
                continue

            obj = Model.objects.filter(pk=pk).first()
            if not obj:
                self.stderr.write(f'Object not found: {model_name} {pk}')
                continue

            try:
                resp = requests.get(url, stream=True, timeout=30)
                resp.raise_for_status()
            except Exception as e:
                self.stderr.write(f'Failed to download {url}: {e}')
                continue

            # determine extension
            ext = os.path.splitext(url.split('?')[0])[1]
            if not ext:
                ct = resp.headers.get('content-type','')
                if 'jpeg' in ct or 'jpg' in ct:
                    ext = '.jpg'
                elif 'png' in ct:
                    ext = '.png'
                else:
                    ext = '.jpg'

            subdir = ''
            if model_name.lower().startswith('beach'):
                subdir = 'beach_images'
            elif model_name.lower().startswith('transport'):
                subdir = 'transport_images'
            elif model_name.lower().startswith('accommodation'):
                subdir = 'accommodation_images'
            elif model_name.lower().startswith('tourist') or model_name.lower().startswith('attraction'):
                subdir = 'attraction_images'
            else:
                subdir = 'images'

            filename = f"{model_name.lower()}_{pk}{ext}"
            media_dir = os.path.join(settings.MEDIA_ROOT, subdir)
            os.makedirs(media_dir, exist_ok=True)
            dest_path = os.path.join(media_dir, filename)

            try:
                with open(dest_path, 'wb') as out_f:
                    for chunk in resp.iter_content(chunk_size=8192):
                        out_f.write(chunk)
            except Exception as e:
                self.stderr.write(f'Error saving file {dest_path}: {e}')
                continue

            # set image field to relative media path
            rel_path = os.path.join(subdir, filename).replace('\\', '/')
            setattr(obj, 'image', rel_path)
            obj.save()
            self.stdout.write(f'Saved image for {model_name} {pk} -> {rel_path}')
