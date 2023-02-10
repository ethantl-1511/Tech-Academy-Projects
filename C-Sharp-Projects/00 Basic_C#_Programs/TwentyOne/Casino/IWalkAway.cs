using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Casino.Interfaces
{
    interface IWalkAway // Note: Naming convention for interface is to start with an I
    {
        void WalkAway(Player player);
    }
}
