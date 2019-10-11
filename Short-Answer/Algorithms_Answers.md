#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
	This is the sumation of n**2 till n**3
	https://www.desmos.com/calculator/w9fzezlelh
	
b)
	the while loop will count up powers of 2 (2^0 2^1 2^2 ... 2^x where sumation of j^x is less then n.
	the top for loop is pointless as you could just take the bottom for loop and multipy by n, there for this
	is a very ineffecient way of saying
	https://www.desmos.com/calculator/ai0odvxbdx

c) 
	assuming bunnies is a positive number (the domain of this function fails at bunnies < 0 as there is no way to break this function)
	this will return 2*bunnies in a recurive function call.

## Exercise II
	If you count the time that it takes to move floors (as part of the algorithm) and if you start on the ground at the beinging.
	Any method that breaks the problem down (like binary algorithm) will only cause more walking for said person, which will increase time.
	There for the quickest way to solve this problem would be to go one floor at a time and drop an egg (of course if we could have multiple people
	ie multiple threads) each drop eggs we could use a more binary approach, which would save time. 
	
	The time complexity come in play as each floor you traverse and dont drop an egg will only hurt the over all completion time, so by going floor by
	floor you are decreasing the chance of a untimely result. Where as if you could move quickly between floors, (ie an elevator) then using a binary 
	approach dividing up or quickly jumping between floors would be a more plausable solution. Or if dropping an egg time was drastically greater
	than the time it take to move over a floor this would also make a binarry approach more plauseable
	
	In conclusion, it comes down to a relationship between cost to drop an egg over cost to move floors. Based on these two factor we can describe the time
	complexity of this algorithm and therefore come up with a most optimized solution.

