# Farey Algorithm

Website: https://farey.netlify.app/

## Summary
We can use the Farey sequences to find rational approximations of irrational numbers.<sup><a href="https://web.archive.org/web/20181119092100/https://nrich.maths.org/6596">1</a></sup> Another trivial use is to convert decimals to fractions.

## Method
For the two positive rational numbers b/d and ac the mediant is defined as a+b/c+d. The mediant has the nice property that it is always in between the two fractions giving rise to it: if 0 < b/d < a/c then b/d < a+b/c+d < ac.

In order to find a rational approximation to an irrational number using Farey fractions you need to pick the interval between Farey fractions that contains the target number and narrow the interval at each step. <sup><a href="https://web.archive.org/web/20181119092100/https://nrich.maths.org/6596">1</a></sup>

### Footnotes

1) <a href="https://web.archive.org/web/20181119092100/https://nrich.maths.org/6596">"Farey Approximation"</a>. NRICH.maths.org. Archived from the original on 19 November 2018. Retrieved 21 February 2021.