class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)

        context['title'] = self.title

        return context


class PathMixin:
    path = None

    def get_context_data(self, **kwargs):
        context = super(PathMixin, self).get_context_data(**kwargs)

        context['path'] = self.path

        return context


class ModelMixin:
    model_text = None

    def get_context_data(self, **kwargs):
        context = super(ModelMixin, self).get_context_data(**kwargs)

        context['text'] = self.model_text

        return context


class IconMixin:
    icons_elem = None

    def get_context_data(self, **kwargs):
        context = super(IconMixin, self).get_context_data(**kwargs)

        context['elements'] = self.icons_elem

        return context


class ImageMixin:
    image = None

    def get_context_data(self, **kwargs):
        queryset = super(ImageMixin, self).get_context_data(**kwargs)

        queryset['image_background'] = self.image

        return queryset
