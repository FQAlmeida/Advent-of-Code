use std::cmp::max;
use std::fs::read_to_string;

const INPUT_FILEPATH: &str = "../input/input.txt";

fn get_calories() -> u64 {
    let mut max_calories = 0u64;
    let mut current_calories = 0u64;

    // TODO(Any): read file lazily
    let file_lines = read_to_string(INPUT_FILEPATH).unwrap();
    let lines = file_lines.lines();

    for line in lines {
        if line.trim().is_empty() {
            max_calories = max(max_calories, current_calories);
            current_calories = 0;
            continue;
        }
        current_calories += line.parse::<u64>().unwrap();
    }
    return max_calories;
}

fn main() {
    println!("Calories {}", get_calories());
}

#[cfg(test)]
mod test {
    use crate::get_calories;

    #[test]
    fn output_should_be_66186() {
        let result = get_calories();
        let true_result = 66186;
        assert_eq!(result, true_result)
    }
}
