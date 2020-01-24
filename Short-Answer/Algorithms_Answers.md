#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime = O(n) Exercise 1.a)because this is linear time, where n is the number of times that the loop happens. We put in 5 and the amount of time the while loop is called is 5 times.


b) Runtime = O(n^2). Exercise 1.b )has a nested loop so I believe that would result in a n squared run time.


c)Runtime = O(n).Exercise 1.c) It a looks to be linear as we have no nested loops and our function is triggering a recursive call for every bunny input into this function. So It is recursive

## Exercise II
- Essentially this would call for a binary search to minmize all of the egg damaged in this process. What we would do is take the floors(starting with 1st floor to whatever highest floor is) and add them up and then divide by 2 to get the middle floor. If this is equal to the floor then we are finished here. We will drop the egg and if it is not broken that means we are lower than floor f. In this case we can eliminate all of the lower floors because we know floor f can never be lower since the egg did not break. If the egg did break then we can eliminate all of the floors above because we know floor f will not be any higher than this floor that the egg broke. We repeat the process until we find floor f.
- Best case scenario is we find the floor for the first time making it an O(1) and the average and worst time will be O(logn) since the input we put will be halved


