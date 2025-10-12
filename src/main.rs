use clap::{Parser, Subcommand};

#[derive(Debug, Parser)]
#[clap(author, version, about)]
struct Args {
    #[clap(subcommand)]
    command: Command,
}

#[derive(Debug, Subcommand)]
enum Command {
    #[clap(about = "Adds two numbers")]
    Add {
        #[clap(help = "The first number")]
        a: i32,
        #[clap(help = "The second number")]
        b: i32,
    }
}

fn main() {
    let args = Args::parse();

    match args.command {
        Command::Add { a, b } => {
            let result = a + b;
            println!("Result: {}", result);
        }
    }
}
