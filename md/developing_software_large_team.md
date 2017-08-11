# Essential roles for developing software with large teams

- Release management
- Implementation
- Support
- Operations
- Quality Assurance
- Project management
- Client manager / advocate

# Heirarchy of roles

- Individual contributor (IC)
  -  implements code changes
  -  occasionally provides technical review
  -  sets weekly, sometimes daily goals with team lead
- Team lead (TL)
  - First level with management responsibilities
  - Not a true manager, but does have input in annual review
  - Responsible for the proficiency and efficiency of self and up to
    three individual contributors
  - Will ensure that technical review is generated for all
    implementation work before it is assigned to ICs.
- Manager
  - Coordinates a team of up to eight, comprised of up to 3 team leads,
    each having up to three individual contributors

# Technical oversight and leadership (technical architecture, TA)

- Responsible for specifying new system components, or significant
  changes in existing componennts
- Technical architects (TA) operate in a heirarchy removed from the ICs.
- TAs provide essential input and support to the work implemented by
  ICs.
- Handles technical discussion of product features and implemenation
  options with external parties which could include product teams in
  other regions, vendors, or core developers.


# Documenting changes and communicating in a large organization.

Perhaps the hardest part of building software is deciding what to build
and how to build it. Of course this have been discussed before here &
here. I've experienced the need for leaving a trail of data and
decisions in multiple circumstances. In each scenario, it eventually
becomes important to understand why code was written.

- What were the assumptions made by the person writing the code?
- What goal were they trying to attain?
- What was the business reason behind making the code change?

Without knowing the answers to those questions, it becomes very hard to
know with certainty whether or not the code is still relevant.

Another point I've noticed is that code often lives for much longer than
the implementer expects it to. Thoughts of "I can come back and improve
this later" will very rarely be realized. I've seen this in large
organizations and small teams.

## Couldn't you know whether code is important simply by how obscure it is?

Surely, if code is tucked away in some branch of the code base that is
hard to reach (logically), then it cannot be very important can it?

Yes! Yes, it could be very important! It's actually very hard to know
whether or not code is needed simply be trying to imagine the way in
which it might be used. Very often, bugs come out of unexpected
conditions in the production environment.
