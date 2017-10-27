# Yu-Gi-Oh

## Logs
10/26/2017
Cleaned up raw card lists, and the cleaned list can be found at *cleaned_cards*

Need to categorize each of the 1610 cards into one of the following categories:
1. Normal Monster
2. Effect Monster
3. Fusion Normal Monster
4. Fusion Effect Monster
5. Trap
6. Spell

Similarly, each effect, trap, or spell card needs to be assigned an *effect ID*, which will denote what effects the card possesses (not exhaustive):
- PNTR (Atk-Def penetration damage)
- DSTR (Destroy a card)
- REMV (Remove a card from play)
- RETR (Return a card to the hand)
- SPSM (Special summon a card)

For the *effect IDs* which require a target card for the card interaction, a *target ID* must also be added to denote what type of cards the effect can or will target:
- MNST (Monster cards)
- TRSP (Trap and spell cards)
- FCUP (Face-up monster cards)
- GVYD (Cards in the graveyard)

For all monster cards, columns are required to denote ATK, DEF, and LVL information.
