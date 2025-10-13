use clap::{Parser, Subcommand};
use dotenv::dotenv;
use reqwest;
use serde_json::Value;
use std::collections::HashMap;
use std::env;

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
    Pause {},
    #[clap(about = "Starts your sound")]
    Start {},
    #[clap(about = "Plays a song")]
    Play {},
    #[clap(about = "Search a song")]
    Search {},
    #[clap(about = "Testing")]
    Test {},
}

// update to take id and secret from .env file
async fn get_access_token() -> Result<String, Box<dyn std::error::Error>> {
    dotenv().ok();
    let client_id = env::var("CLIENT_ID").expect("CLIENT_ID not set");
    let client_secret = env::var("CLIENT_SECRET").expect("CLIENT_SECRET not set");
    let client = reqwest::Client::new();

    let mut parms = HashMap::new();
    parms.insert("grant_type", "client_credentials");
    parms.insert("client_id", client_id.as_str());
    parms.insert("client_secret", client_secret.as_str());

    let res = client
        .post("https://accounts.spotify.com/api/token")
        .header("Content-type", "application/x-www-form-urlencoded")
        .form(&parms)
        .send()
        .await?;

    let body = res.text().await?;

    let json: serde_json::Value = serde_json::from_str(&body)?;
    let access_token = json["access_token"]
        .as_str()
        .ok_or("access token not found")?
        .to_string();

    Ok(access_token)
}

// update to take in user input: ie, track name or album name or artist
async fn serach_track(access_token: &String) -> Result<(), Box<dyn std::error::Error>> {
    //jq query to get names of songs: .tracks["items"][]["album"] | select(.album_type == "single") | ."name"
    let client = reqwest::Client::new();

    let bearer_token = "Bearer ".to_owned() + access_token;

    let res = client
        // .get("https://api.spotify.com/v1/search?q=remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davis&type=track")
        .get("https://api.spotify.com/v1/search?q=track%3AYEAH%2BRIGHT&type=track&market=US")
        .header("Authorization", bearer_token)
        .send()
        .await?;

    println!("Status: {}", res.status());

    // let body = res.text().await?;
    //
    // println!("{:?}", body);

    let json: Value = res.json().await?;
    // let tracks = json["tracks"]
    //     .as_str()
    //     .ok_or("tracks not found")?
    //     .to_string();
    //
    // println!("{:?}", tracks);
    println!("{:#?}", json);

    Ok(())
}

#[tokio::main]
async fn main() {
    let args = Args::parse();
    let response = get_access_token().await;

    match args.command {
        // Command::Add { a, b } => {
        //     let result = a + b;
        //     println!("Result: {}", result);
        // }
        Command::Pause {} => {
            println!("Will pause your song");
        }
        Command::Start {} => {
            println!("Will start your song");
        }
        Command::Play {} => {
            println!("Plays a song");
        }
        Command::Search {} => {
            println!("Search a song");
        }
        Command::Test {} => {
            let _ = serach_track(&response.unwrap()).await;
        }
    }
}
