from rich.console import Console

console=Console()

def show_dashboard():

    console.clear()

    console.rule("[bold cyan]ATLAS[/bold cyan]")

    console.print("سیستم عامل تصمیم گیری",style="green")

    console.print()

    console.print("1. ثبت حافظه")

    console.print("2. مشاهده حافظه ها")

    console.print("3. خروج")

    console.print()