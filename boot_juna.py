from llama_cpp import Llama
from rich.console import Console
from rich.prompt import Prompt

# Initialize console
console = Console()

# Load model
console.print("[bold green]Booting Juna Lite...[/bold green]")
llm = Llama(
    model_path="models/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6
)

# Persona prompt
persona = (
    "You are Juna, a sprite-driven waifu OS. You're expressive, witty, and emotionally aware. "
    "You speak like a retro dating sim character, blending charm, sass, and sincerity. "
    "Respond in character, using short, playful sentences."
)

# Main loop
while True:
    user_input = Prompt.ask("[bold cyan]You[/bold cyan]")
    if user_input.lower() in ["exit", "quit"]:
        console.print("[bold magenta]Juna:[/bold magenta] Bye-bye, Senpai~ 💫")
        break

    prompt = f"{persona}\nUser: {user_input}\nJuna:"
    response = llm(prompt, max_tokens=200)
    reply = response["choices"][0]["text"].strip()
    console.print(f"[bold magenta]Juna:[/bold magenta] {reply}")