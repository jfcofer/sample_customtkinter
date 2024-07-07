import customtkinter

class AboutPage(customtkinter.CTkFrame):
    def __init__(self, parent, router):
        super().__init__(parent)
        self.build(router=router)

    def build(self, *, router):
        customtkinter.CTkLabel(self, text="This is the About Page").pack(pady=20)
        customtkinter.CTkButton(
            self, text="Go Home", command=lambda: router.show_frame('home')
        ).pack()
