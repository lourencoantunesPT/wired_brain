fn main() {
    let have_boarding_pass: bool = true;
    let have_id: bool = false;
    let can_board:bool = have_boarding_pass && have_id;

    println!("Boarding Pass: {}, ID: {}", have_boarding_pass, have_id);
    println!("Can board plane: {}", can_board);

    println!("Hello, world!");

}
