//use std::error::Error;
use std::fs::File;
//use std::path::Path;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("1.txt")?;
    let reader = BufReader::new(file);
    let mut acc = 0;
    for line in reader.lines() {
        let mut my_int = line?.parse::<i32>().unwrap();
        acc = acc + calculate_fuel(my_int);
    }

    print!("{}",acc);

    Ok(())
}

fn calculate_fuel(x: i32) -> i32 {
    let mut output = x;
    output /= 3;
    output -= 2;
    let o = output;
    if o >= 0 {
        print!("{}\n",o);
        o + calculate_fuel(o)
    }
    else{
        0
    }
}