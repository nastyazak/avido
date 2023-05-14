class UserStatus:
    blocked = 'blocked'
    active = 'active'
    waiting = 'waiting'

    CHOICES = (
        (blocked, 'blocked'),
        (active, 'active'),
        (waiting, 'waiting'),
    )


class AdStatus:
    draft = 'draft'
    moderate = 'moderate'
    rejected = 'rejected'
    withdrawn = 'withdrawn'
    active = 'active'

    CHOICES = (
        (draft, 'draft'),
        (moderate, 'moderate'),
        (rejected, 'rejected'),
        (withdrawn, 'withdrawn'),
        (active, 'active'),
    )