using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Casino
{
    public class Dealer
    {
        public string Name { get; set; }
        public Deck Deck { get; set; }
        public int Balance { get; set; }

        public void Deal(List<Card> Hand)
        {
            Hand.Add(Deck.Cards.First()); // hand is a list, we are adding a card to the hand ... we add first item
            string card = string.Format(Deck.Cards.First().ToString() + "\n");
            Console.WriteLine(card); // the card about to be added to the deck ... we print to console
            //using (StreamWriter file = new StreamWriter(@"[file path]", true)) // log creation
            //{
            //    file.WriteLine(DateTime.Now);
            //    file.WriteLine(card);
            //}
            Deck.Cards.RemoveAt(0); // pass in an index we want to remove ... we remove from deck
        }
    }
}
