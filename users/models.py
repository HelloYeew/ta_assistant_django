from django.db import models
from django.contrib.auth.models import User
from PIL import Image

ROLE = (
    # In-system value - Show value
    ('student', "STUDENT"),
    ('teacher', "TEACHER")
)

CODE_HIGHLIGHT = (
    ('a11y-dark', 'A11Y Dark'),
    ('a11y-light', 'A11Y Light'),
    ('agate', 'Agate'),
    ('an-old-hope', 'An Old Hope'),
    ('androidstudio', 'Android Studio'),
    ('arduino-light', 'Arduino Light'),
    ('arta', 'Arta'),
    ('ascetic', 'Ascetic'),
    ('atelier-cave-dark', 'Atelier Cave Dark'),
    ('atelier-cave-light', 'Atelier Cave Light'),
    ('atelier-dune-dark', 'Atelier Dune Dark'),
    ('atelier-dune-light', 'Atelier Dune Light'),
    ('atelier-estuary-dark', 'Atelier Estuary Dark'),
    ('atelier-estuary-light', 'Atelier Estuary Light'),
    ('atelier-forest-dark', 'Atelier Forest Dark'),
    ('atelier-forest-light', 'Atelier Forest Light'),
    ('atelier-health-dark', 'Atelier Health Dark'),
    ('atelier-health-light', 'Atelier Health Light'),
    ('atelier-lakeside-dark', 'Atelier Lakeside Dark'),
    ('atelier-lakeside-light', 'Atelier Lakeside Light'),
    ('atelier-plateau-dark', 'Atelier Plateau Dark'),
    ('atelier-plateau-light', 'Atelier Plateau Light'),
    ('atelier-savanna-dark', 'Atelier Savanna Dark'),
    ('atelier-savanna-light', 'Atelier Savanna Light'),
    ('atelier-seaside-dark', 'Atelier Seaside Dark'),
    ('atelier-seaside-light', 'Atelier Seaside Light'),
    ('atelier-sulphurpool-dark', 'Atelier Sulphurpool Dark'),
    ('atelier-sulphurpool-light', 'Atelier Sulphurpool Light'),
    ('atom-one-dark-reasonable', 'Atom One Dark Reasonable'),
    ('atom-one-dark', 'Atom One Dark'),
    ('atom-one-light', 'Atom One Light'),
    ('brown-paper', 'Brown Paper'),
    ('codepen-embed', 'Codepen Embed'),
    ('color-brewer', 'Color Brewer'),
    ('darcula', 'Darcula'),
    ('dark', 'Dark'),
    ('default', 'Default'),
    ('far', "Far"),
    ('foundation', "Foundation"),
    ('github', 'GitHub'),
    ('github-gist', 'GitHub Gist'),
    ('gml', 'GML'),
    ('googlecode', 'Google Code'),
    ('gradient-dark', 'Gradient Dark'),
    ('gradient-light', 'Gradient Light'),
    ('grayscale', 'Grayscale'),
    ('gruvbox-dark', 'Gruvbox Dark'),
    ('gruvbox-light', 'Gruvbox Light'),
    ('hopscotch', "hopscotch"),
    ('hybrid', "Hybrid"),
    ('idea', "Idea"),
    ('ir-black', "IR Black"),
    ('isbl-editor-dark', 'ISBL Editor Dark'),
    ('isbl-editor-light', 'ISBL Editor Light'),
    ('kimbie.dark', 'Kimbie Dark'),
    ('kimbie.light', 'Kimbie Light'),
    ('lightfair', 'Lightfair'),
    ('lioshi', 'Lioshi'),
    ('magula', 'Magula'),
    ('mono-blue', 'Mono Blue'),
    ('monokai-sublime', 'Monokai Sublime'),
    ('monokai', 'Monokai'),
    ('night-owl', 'Night Owl'),
    ('nnfx', 'NNFX'),
    ('nnfx-dark', 'NNFX Dark'),
    ('nord', 'Nord'),
    ('obsidian', 'Obsidian'),
    ('ocean', 'Ocean'),
    ('paraiso-dark', 'Paraiso Dark'),
    ('paraiso-light', 'Paraiso Light'),
    ('pojoaque', 'Pojoaque'),
    ('purebasic', 'Pure Basic'),
    ('qtcreator_dark', 'QTCreator Dark'),
    ('qtcreator_light', 'QTCreator Light'),
    ('railscasts', 'Railscasts'),
    ('rainbow', 'Rainbow'),
    ('routeros', 'Routeros'),
    ('school-book', 'School Book'),
    ('shades-of-purple', 'Shades of Purple'),
    ('solarized-dark', 'Solarized Dark'),
    ('solarized-light', 'Solarized Light'),
    ('srcery', 'Srcery'),
    ('stackoverflow-dark', 'Stackoverflow Dark'),
    ('stackoverflow-light', 'Stackoverflow Light'),
    ('sunburst', 'Sunburst'),
    ('tomorrow-night-', 'Tomorrow Night-'),
    ('tomorrow-night-blue', 'Tomorrow Night Blue'),
    ('tomorrow-night-bright', 'Tomorrow Night Bright'),
    ('tomorrow-night-eighties', 'Tomorrow Night Eighties'),
    ('vs', 'Visual Code'),
    ('vs2015', 'Visual Code 2015'),
    ('xcode', 'XCode'),
    ('xt256', 'XT256'),
    ('zenburn', 'Zenburn'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(default='6000000000')
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    role = models.CharField(max_length=10, choices=ROLE, default='student', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# TODO: Make auto resize picture system


class Config(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_highlight = models.CharField(max_length=50, choices=CODE_HIGHLIGHT, default='atom-one-dark')

    def __str__(self):
        return f'{self.user.username} Config'