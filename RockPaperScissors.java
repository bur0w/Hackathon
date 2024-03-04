import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            // Get move choice from Player A
            String moveA = getPlayerMove("Player A", scanner);
            
            // Get move choice from Player B
            String moveB = getPlayerMove("Player B", scanner);
            
            // Display moves
            System.out.println("Player A chose: " + moveA);
            System.out.println("Player B chose: " + moveB);
            
            // Determine winner
            String result = determineWinner(moveA, moveB);
            System.out.println(result);
            
            // Prompt user to play again
            System.out.print("Do you want to play again? (Y/N): ");
            String playAgain = scanner.next();
            
            if (!playAgain.equalsIgnoreCase("Y")) {
                System.out.println("Thanks for playing!");
                break;
            }
        }
        
        scanner.close();
    }
    
    public static String getPlayerMove(String playerName, Scanner scanner) {
        String move;
        while (true) {
            System.out.print(playerName + ", enter your move (R for Rock, P for Paper, S for Scissors): ");
            move = scanner.next().toUpperCase();
            if (move.equals("R") || move.equals("P") || move.equals("S")) {
                break;
            } else {
                System.out.println("Invalid move. Please enter R, P, or S.");
            }
        }
        return move;
    }
    
    public static String determineWinner(String moveA, String moveB) {
        if (moveA.equals(moveB)) {
            return "It's a Tie!";
        } else if ((moveA.equals("R") && moveB.equals("S")) ||
                   (moveA.equals("P") && moveB.equals("R")) ||
                   (moveA.equals("S") && moveB.equals("P"))) {
            return "Player A wins!";
        } else {
            return "Player B wins!";
        }
    }
}
