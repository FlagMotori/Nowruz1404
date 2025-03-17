# Blackmirror

## Description
Are you interested in **black mirror** serie? if yes, then come up here to index the episodes


## Solution
The intended solution is to use the **Mysql Special Comments**, that can execute sql

The reason of that, its beacause the format of this kind of comment is: `/*! Sql */`
and because of mirrorifying queries, the result of `/*! Sql */` becomes to this `/* lqS !*/`, and thats a valid statement
Note: because of wrapping the query in the parenthese `()` in the **LIKE** statement, the final query ends up with `()`

For example:
```
query: A") /*! sql */
final: SELECT * FROM series WHERE name LIKE ("%A") /*! sql *//* lqs !*/ ("A%")
```

But this is not an valid query because of the last `("A%")` in the query, and that will fix by adding a plus `(+)` at the end of your query

for example:
```
query: %A") /*! sql */ +
final: SELECT * FROM series WHERE name LIKE ("%A") /*! sql */ ++ /* lqs !*/ ("A%")
```

Checkout the [exploit.py](chall/exploit.py)
