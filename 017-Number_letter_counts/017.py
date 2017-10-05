onetonine = "onetwothreefourfivesixseveneightnine"
tentonineteen = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
twentytoninety = "twentythirtyfortyfiftysixtyseventyeightyninety"
hundred = "hundred"
thousand = "thousand"
_and = "and"

print(len("one") + len(thousand) + 900*len(hundred) + 100*len(onetonine) + 100*len(twentytoninety) +\
      891*len(_and) + 80*len(onetonine) + 10*(len(onetonine) + len(tentonineteen)))