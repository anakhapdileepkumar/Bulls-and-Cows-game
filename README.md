# 🐂 Bulls and Cows – Python Game  

## 🎯 Objective  
Guess the secret 4-digit number (digits 1–9, no repeats).  
You get **Bulls** for correct digits in the right position and **Cows** for correct digits in the wrong position.  


## 📜 Rules  
1. The computer randomly picks a **4-digit number** (digits from 1–9, no duplicates, no zero).  
2. You enter a guess.  
3. The program tells you:  
   - **Bulls** → correct digit in the **correct position**.  
   - **Cows** → correct digit in the **wrong position**.  
4. Keep guessing until you find the number.  


## 💡 Example  
Secret: `5732`  
Guess: `5378`  
- **Bulls** → `5` and `7` (right position) → **2 Bulls**  
- **Cows** → `3` (right digit, wrong position) → **1 Cow**  
Output: `2 Bulls, 1 Cow`
