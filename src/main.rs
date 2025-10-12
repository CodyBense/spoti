use clap::{Parser, Subcommand};

#[derive(Parser, Debug)]
#[command(author = "Cody Bense", version = "1.0")]
struct Args {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand, Debug)]
enum Command {
    #[command(name = "add")]
    Add {
        #[arg(short, long)]
        a: i32,
        #[arg(short, long)]
        b: i32,
    },
    #[command(name = "sub")]
    Subtract {
        #[arg(short, long)]
        a: i32,
        #[arg(short, long)]
        b: i32,
    },
}

fn main() {
    let args = Args::parse();
    match args.command {
        Command::Add { a, b } => println!("Result: {}", a + b),
        Command::Subtract { a, b } => println!("Result: {}", a - b),
    }
}
