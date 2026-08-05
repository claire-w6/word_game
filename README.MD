### Game Rules

This is a game I usually play with my friends when we are bored waiting in line. The rules are to say a word, and the next person has to think of a word that has not been said before and it matches the last letter of the previous word.

I personally think this is a good game to learn new words and keep your mind fresh!

### Enhancements
- [ ] Create Second Player
- [ ] Create Hints
- [ ] Give definition if not known
- [ ] Create a UI
- [x] Add a counter score
- [x] Highest score board
- [ ] Play again key
- [ ] Max 3 wrong

### To Fix
- [ ] Scoreboard doesn't persist after each play through

## Design Process
User inputs first word -> word goes into a used word bank if a valid word, otherwise return error

## What I would do better in the future
I liked using a set for the used words bank since all the words should ideally be unique and the order doesn't matter. I would ideally use a key on the keyboard to exit out of the game rather than use a safe word to exit. I would also like to refactor the code so that it's less convoluted.
