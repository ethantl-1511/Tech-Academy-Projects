using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using CarInsurance.Models;

namespace CarInsurance.Controllers
{
    public class InsureeController : Controller
    {
        private InsuranceEntities db = new InsuranceEntities();

        // GET: Insuree
        public ActionResult Index()
        {
            return View(db.Insurees.ToList());
        }

        // GET: Insuree/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Insuree insuree = db.Insurees.Find(id);
            if (insuree == null)
            {
                return HttpNotFound();
            }
            return View(insuree);
        }

        // GET: Insuree/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Insuree/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "Id,FirstName,LastName,EmailAddress,DateOfBirth,CarYear,CarMake,CarModel,DUI,SpeedingTickets,CoverageType,Quote")] Insuree insuree)
        {
            if (ModelState.IsValid)
            {
                // logic to calculate quote based on conditions--
                decimal quoteTotal = 50m; // quote base total (per month)
                // age logic
                int currentYear = DateTime.Now.Year; // current year for determining age of user
                DateTime insureeDOB = insuree.DateOfBirth; // grab the DateOfBirth information from insurees, sets as individual insureeDOB
                int insureeDOBYear = insureeDOB.Year; // gets the insuree's exact birth year
                int insureeAge = currentYear - insureeDOBYear; // birth year - current year = now we have insuree's age
                if (insureeAge < 18)
                {
                    quoteTotal += 100m; // adds 100 to total
                }
                if (insureeAge >= 19 && insureeAge <= 25)
                {
                    quoteTotal += 50m; // adds 50 to total
                }
                if (insureeAge >= 26)
                {
                    quoteTotal += 25m; // adds 25 to total
                }
                // car year logic
                if (insuree.CarYear < 2000)
                {
                    quoteTotal += 25m;
                }
                if (insuree.CarYear > 2015)
                {
                    quoteTotal += 25m;
                }
                // car make logic
                if (insuree.CarMake == "Porsche" || insuree.CarMake == "porsche")
                {
                    quoteTotal += 25m;
                }
                if (insuree.CarMake == "Porsche" || insuree.CarMake == "porsche" && insuree.CarModel == "911 Carrera" || insuree.CarModel == "911 carrera")
                {
                    quoteTotal += 25m;
                }
                // ticket logic
                if (insuree.SpeedingTickets > 0)
                {
                    int tickets = insuree.SpeedingTickets; // set ticket number to int
                    quoteTotal += (tickets * 10m); // add (tickets * 10) to quoteTotal
                }
                // DUI and coverage bool logic
                if (insuree.DUI == true)
                {
                    quoteTotal += (quoteTotal * 0.25m); // takes current total, e.g. 100, multiplies it by 0.25 (25%), then adds it to quoteTotal.
                }
                if (insuree.CoverageType == true)
                {
                    quoteTotal += (quoteTotal * 0.5m);
                }
                insuree.Quote = quoteTotal; // sets insuree Quote as the quoteTotal, overwrites whatever is typed into Quote field

                db.Insurees.Add(insuree);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(insuree);
        }

        // GET: Insuree/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Insuree insuree = db.Insurees.Find(id);
            if (insuree == null)
            {
                return HttpNotFound();
            }
            return View(insuree);
        }

        // POST: Insuree/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id,FirstName,LastName,EmailAddress,DateOfBirth,CarYear,CarMake,CarModel,DUI,SpeedingTickets,CoverageType,Quote")] Insuree insuree)
        {
            if (ModelState.IsValid)
            {
                db.Entry(insuree).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(insuree);
        }

        // GET: Insuree/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Insuree insuree = db.Insurees.Find(id);
            if (insuree == null)
            {
                return HttpNotFound();
            }
            return View(insuree);
        }

        // POST: Insuree/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Insuree insuree = db.Insurees.Find(id);
            db.Insurees.Remove(insuree);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        public ActionResult Admin()
        {
            return View(db.Insurees.ToList());
        }
    }
}
