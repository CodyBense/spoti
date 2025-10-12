use clap::{Parser, Subcommand};

#[derive(Debug, Parser)]
#[clap(
    author = "Cody Bense",
    version = "0.1.0",
    about = "A silly little cli to control your spotify from the terminal instead of using the app"
)]
struct Args {
    #[clap(subcommand)]
    command: Command,
}

#[derive(Debug, Subcommand)]
enum Command {
    // #[clap(about = "Adds two numbers")]
    // Add {
    //     #[clap(help = "The first number")]
    //     a: i32,
    //     #[clap(help = "The second number")]
    //     b: i32,
    // },
    #[clap(about = "Pauses your sound")]
    Pause {
    },
    #[clap(about = "Starts your sound")]
    Start {
    },
    #[clap(about = "Plays a song")]
    Play {
    },
    #[clap(about = "Search a song")]
    Search {
    },
}

fn main() {
    let args = Args::parse();

    match args.command {
        // Command::Add { a, b } => {
        //     let result = a + b;
        //     println!("Result: {}", result);
        // }
        Command::Pause {  } => {
            println!("Will pause your song");
        },
        Command::Start {  } => {
            println!("Will start your song");
        },
        Command::Play {  } => {
            println!("Plays a song");
        },
        Command::Search {  } => {
            println!("Search a song");
        },
    }
}
