use std::collections::HashMap;
//use std::error::Error;
use std::fs::File;
//use std::path::Path;
use std::io::{self, prelude::*, BufReader};

fn main(){
    let mut op_codes = HashMap::new();
    let mut acc = 0;
    let file = File::open("2.txt")?;
    let reader = BufReader::new(file);
    for line in reader.lines()[0].split(',') {
        let mut my_int = line?.parse::<i32>().unwrap();
        op_codes.insert(acc.to_string(),my_int.to_string());
        print!("{}",acc);
        acc+= 1;
    }
}