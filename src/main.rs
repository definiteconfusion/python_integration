use std::env;
use meval::eval_str;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 4 {
        eprintln!("Usage: <program> <eq> <acc> <start>");
        std::process::exit(1);
    }
    let eq = &args[1]; 
    let acc: f64 = args[2].parse().expect("Failed to parse 'acc' as f64");
    let start: f64 = args[3].parse().expect("Failed to parse 'start' as f64");
    let strt_repl = eq.replace("x", &start.to_string());
    match eval_str(&strt_repl) {
        Ok(start_rslt) => {
            let end_repl = eq.replace("x", &(start + acc).to_string());
            match eval_str(&end_repl) {
                Ok(end_rslt) => {
                    let result = (end_rslt * acc) + (acc * (start_rslt - end_rslt));
                    println!("{}", result);
                }
                Err(e) => {
                    eprintln!("Failed to evaluate equation at end value: {}", e);
                    std::process::exit(1);
                }
            }
        }
        Err(e) => {
            eprintln!("Failed to evaluate equation at start value: {}", e);
            std::process::exit(1);
        }
    }
}
