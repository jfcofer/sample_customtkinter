import customtkinter



class HomePage(customtkinter.CTkFrame):

    def __init__(self, master, router):
        super().__init__(master)
        self.build(router=router)

    def build(self, *, router):
        customtkinter.CTkLabel(self, text="This is the Home Page").pack(pady=20)
        customtkinter.CTkButton(
            self, text="Go to About", command=lambda: router.show_frame("about")
        ).pack()
        customtkinter.CTkButton(
            self, text="Go to Contact", command=lambda: router.show_frame("contact")
        ).pack()
