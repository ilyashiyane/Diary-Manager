import questionary
from questionary import Style
from rich.console import Console
from rich.align import Align
def Admin() :
        while True :
            console=Console()
            console.print(Align("Admin dashboard",align="center",style="italic green"))
            #console.print("Admin dashboard")
            custom_style = Style([
    ("question", "bold fg:#FFFF00"),  # jaune + bold
])
            choice = questionary.select(
    "Choose an option:(press control c in order to go back while putting inputs)",
    choices=[
        "👥 Show all users",
        "🗑️ Delete a user",
        "➕ Add a user",
        "🔒 Log out",
        #"❌ Exit"
    ],
    style=custom_style
).ask()
             
            if choice == "👥 Show all users":
                    from .show_users import ShowUsers
                    ShowUsers()
                    console.input(Align("Press to continue",align="center",style="bold yellow"))
            elif choice == "🗑️ Delete a user":
                    from .delete_admin import DeleteAdmin
                    DeleteAdmin()
            elif choice == "➕ Add a user":
                    from .add_user import AddUser
                    AddUser()
                    
            elif choice == "🔒 Log out":
                    print("Logging out...")
                    from .user_creation import connect
                    connect()
                    
            