import json, os
from django.core.management.base import BaseCommand
from django.conf import settings
from shoes.models import RunningShoe

class Command(BaseCommand):
    help = 'Import shoes into the database from shoes.json'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'shoes.json')
        with open(file_path, 'r') as f:
            data = json.load(f)

        for s in data:
            # map JSON → model fields, with defaults for anything missing
            drop_mm = s.get('heel_to_toe_drop', 0)
            weight = s.get('weight_grams', 0)
            surface = s.get('surface', 'unknown')
            foot_strike = s.get('foot_strike', 'unknown')
            pronation = s.get('pronation_support', False)
            image = s.get('image_url', '')

            RunningShoe.objects.create(
                brand=s['brand'],
                model_name=s['model_name'],
                category=s['category'],
                cushioning=s['cushioning'],
                drop_mm=drop_mm,
                weight_grams=weight,
                surface=surface,
                foot_strike=foot_strike,
                pronation_support=pronation,
                image_url=image,
                stack_height=s['stack_height'],
                heel_to_toe_drop=s['heel_to_toe_drop'],
                best_for=s['best_for']
            )

        self.stdout.write(self.style.SUCCESS('Shoes imported successfully!'))
