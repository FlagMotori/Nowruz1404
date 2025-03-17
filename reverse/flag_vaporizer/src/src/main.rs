use std::io::Bytes;

fn is_flag(lu8 : &[u8])->bool{
    let l : Vec<i32> = lu8.iter().map(|byte| i32::from(byte.clone())).collect();
    
    if l[0] + 55 != l[39]{
        return false;
    }

    if l[0] + 31 != l[38]{
        return false;
    }

    if l[2] + 30 != l[35]{
        return false;
    }

    if l[4] * 2 != l[20] + 29{
        return false;
    }

    if l[17] - 25 != l[0]{
        return false;
    }

    if l[32] + 7 != l[39]{
        return false;
    }

    if l[28] / 2 != l[16] - 54{
        return false;
    }

    if l[9] != l[25] - 10{
        return false;
    }

    if l[1] + l[10] - l[20] != l[36] - 31{
        return false;
    }

    if l[1] + l[10] - l[20] != l[36] - 31{
        return false;
    }

    if l[2] - l[12] + l[0] != 42{
        return false;
    }

    if l[3] - l[12] + l[22] != 104{
        return false;
    }

    if l[4] - l[12] + l[23] != l[22] - 45{
        return false;
    }

    if l[5] + l[10] + l[4] - l[11] != 184{
        return false;
    }

    if l[5] + l[9] - l[0] != l[3] + 76{
        return false;
    }

    if l[22] - l[12] + l[35] - l[0] != 47{ 
        return false;
    }

    if l[22] - l[11] + l[2] != l[0] + 2 {
        return false;
    }

    if l[23] - l[22] + l[10] != 81 {
        return false;
    }

    if l[36] + l[10] + l[11] - l[38] != 208{
        return false;
    }

    if l[7] + l[6] + l[17] - l[0] != 237{
        return false;
    }

    if l[10] + l[38] - l[9] != 95 {
        return false;
    }

    if l[20] + l[4] - l[8] != 70 {
        return false;
    }

    if l[11] + l[38] - l[22] + l[7] != l[21] + 101 {
        return false;
    }

    if l[21] + l[33] + l[0] != 276 {
        return false;
    }

    if l[33] + l[32] + l[39] != l[8] + l[10] + 128 {
        return false;
    }

    if l[19] + l[12] + l[17] - l[38] != 205 {
        return false;
    }

    if l[18] + l[36] + l[0] - l[22] != 150 {
        return false;
    }

    if l[16] + l[22] != l[20] + 115 {
        return false;
    }

    if l[22] - l[32] + l[13] != l[9] - 5 {
        return false;
    }

    if l[22] ^ l[24] != 17 {
        return false;
    }

    if l[23] ^ l[0] + l[24] != 247 {
        return false;
    }

    if l[25] + l[20] ^ l[10] != (l[22] ^ l[24]) + 112 {
        return false;
    }

    if l[26] + l[27] ^ l[0] + l[1] != 64 {
        return false;
    }

    if l[26] ^ l[7] != 6 {
        return false;
    }

    if l[27] - l[33] + l[16] != 109 {
        return false;
    }

    if l[28] + l[22] - l[10] != 128 {
        return false;
    }

    if l[29] ^ l[27] != 58 {
        return false;
    }

    if l[30] + l[15] - l[20] != 104 {
        return false;
    }

    if l[31] ^ l[33] != 14 {
        return false;
    }

    if l[34] - l[17] + l[13] != l[8] + 13 {
        return false;
    }

    if l[37] + l[29] - (l[9] ^ l[39]) != 187{
        return false;
    }

    if l[14] + l[22] - l[38] != 124 {
        return false;
    }

    if l[15] + l[21] - (l[20] ^ l[10]) != 215 {
        return false;
    }

    true
}
fn main() {
   let mut line = String::new();
   println!("gimme your flag");
   let b1 = std::io::stdin().read_line(&mut line).unwrap();

   let flag_bytes = line.as_bytes();
   println!("{}\n", is_flag(flag_bytes));

}
