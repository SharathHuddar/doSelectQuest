from rest_framework.renderers import BaseRenderer


class ImageRenderer(BaseRenderer):
    media_type = 'image/*'
    format = '*'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
