from pygame.font import Font


class Text:
    _BODY_STD = None
    _TITLE = None

    @classmethod
    def title(cls):
        if cls._TITLE is None:
            cls._TITLE = Font("assets/fonts/Inter-SemiBold.ttf", size=30)
        return cls._TITLE

    @classmethod
    def body_std(cls):
        if cls._BODY_STD is None:
            cls._BODY_STD = Font("assets/fonts/Inter-Regular.ttf", size=30)
        return cls._BODY_STD
