from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, IntPrompt, Prompt
from asciiscape import imgUtils as iu

console=Console()
def renderTitle():
    title=r'''
╔═╗╔═╗╔═╗╦╦┌─┐┌─┐┌─┐┌─┐┌─┐
╠═╣╚═╗║  ║║└─┐│  ├─┤├─┘├┤ 
╩ ╩╚═╝╚═╝╩╩└─┘└─┘┴ ┴┴  └─┘
'''
    console.print("\n".join(line.center((console.size[0])) for line in title.splitlines()))
    console.print(Panel("Type the [red]PATH[/red] of the [dark_blue]IMAGE[/dark_blue]"), justify="center")

def renderOptions():
    console.print(Panel('''----STYLE----
                        \n[red]C[/red][bright_yellow]O[/bright_yellow][bright_green]L[/bright_green][bright_blue]O[/bright_blue][magenta]R[/magenta] or [grey30]GRAYSCALE[/grey30]
                            \n----CHARSET----
                            \n[blue1]BIG[/blue1] or [deep_sky_blue1]SMALL[/deep_sky_blue1] or [blue_violet]BRAILLE[/blue_violet]
                         ''', title="OPTIONS"), justify="center")
    colorMode=Prompt.ask("[red]C[/red][bright_yellow]O[/bright_yellow][bright_green]L[/bright_green][bright_blue]O[/bright_blue][magenta]R[/magenta] or [grey30]GRAYSCALE[/grey30]", choices=["color", "gray"], default="color", show_default=False)
    charset=Prompt.ask("[blue1]BIG[/blue1] or [deep_sky_blue1]SMALL[/deep_sky_blue1] or [blue_violet]BRAILLE[/blue_violet]", choices=["big", "small", "braille"], default="small", show_default=False)
    if charset=="braille":
        threshold=-1
        dither=Confirm.ask("[medium_purple4]DITHER[/medium_purple4]?")
        while threshold>255 or threshold<0:
            threshold=IntPrompt.ask("[dark_magenta]THRESHOLD[/dark_magenta] [cyan1](0-255)[/cyan1]", default=150, show_default=False)
            return colorMode, charset, dither, threshold
    threshold=0
    dither=False
    return colorMode, charset, dither, threshold

def printAscii(resizedImageArray, color, charset, isDither, threshold):
    if isDither:
        resizedImageArray=iu.ditherImage(resizedImageArray)
        
    if charset=="braille" and color=="color":
        brailleImageArray, brailleImageRGB=iu.imgToAsciiBraille(resizedImageArray, threshold)
        brailleShape=brailleImageArray.shape
        for i in range(brailleShape[0]):
            for j in range(brailleShape[1]):
                console.print(brailleImageArray[i][j][0], end="", style=f"rgb({brailleImageRGB[i][j][0]},{brailleImageRGB[i][j][1]},{brailleImageRGB[i][j][2]})")
            print("")
            
    elif charset=="braille":
        brailleImageArray, brailleImageRGB=iu.imgToAsciiBraille(resizedImageArray, threshold)
        brailleShape=brailleImageArray.shape
        for i in range(brailleShape[0]):
            for j in range(brailleShape[1]):
                console.print(brailleImageArray[i][j][0], end="")
            print("")
            
    elif charset=="big" and color=="color":
        asciiImageArray=iu.imgToAsciiBig(resizedImageArray)
        shape=asciiImageArray.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                console.print(asciiImageArray[i][j], end="", style=f"rgb({resizedImageArray[i][j][0]},{resizedImageArray[i][j][1]},{resizedImageArray[i][j][2]})")
            print()
    
    elif charset=="big":
        asciiImageArray=iu.imgToAsciiBig(resizedImageArray)
        shape=asciiImageArray.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                console.print(asciiImageArray[i][j], end="")
            print()
            
    elif charset=="small" and color=="color":
        asciiImageArray=iu.imgToAsciiSmall(resizedImageArray)
        shape=asciiImageArray.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                console.print(asciiImageArray[i][j], end="", style=f"rgb({resizedImageArray[i][j][0]},{resizedImageArray[i][j][1]},{resizedImageArray[i][j][2]})")
            print()
            
    else:
        asciiImageArray=iu.imgToAsciiSmall(resizedImageArray)
        shape=asciiImageArray.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                console.print(asciiImageArray[i][j], end="")
            print()