## KB-001 — What is FOMO?
Applies to: Platform overview

FOMO is a social networking platform where people post short written updates with an optional photo or video,
follow each other, become friends, and chat privately in real time. Its tagline is "Authentic Connections".

It is used through a web browser. There is no mobile app; the site is responsive and works on a phone browser, but
everything described in this knowledge base is a web experience.

The platform has five pillars:

- A public feed. Anyone with an account can post, and every published post is visible to everyone.
- A social graph with two layers. Following is one-way and instant; friendship is mutual and requires acceptance.
- Private messaging. One-to-one conversations with file attachments, emoji reactions and read receipts, delivered live.
- Activity notifications. Six kinds of alert covering likes, comments, replies, follows and friend requests.
- Discovery. People search, a featured-creators list, and trending hashtags.

Related: KB-002, KB-005, KB-006

## KB-002 — What can I do on FOMO?
Applies to: Platform overview, Feature tour

A complete list of what an ordinary account can do:

Post and interact
- Write a post of up to 10,000 characters, with one photo or video attached
- Edit or delete your own posts
- Archive a post to hide it from everyone but yourself, then unarchive it later
- Like any post, and unlike it again
- Comment on any post, and reply to a comment
- Share (repost) someone else's post, optionally with your own caption

Build a network
- Follow anyone, with no approval needed
- Send, accept, reject and cancel friend requests
- Unfriend, and see anyone's followers, following and friends lists
- Search for people by username, browse featured creators, and see trending hashtags

Talk privately
- Start a one-to-one conversation with anyone on the platform
- Send messages up to 5,000 characters with photo, video or document attachments
- Edit and delete your own messages, and react to any message with an emoji

Manage your identity
- Set a display name, a bio, a profile photo and a cover photo
- Change your username

Things FOMO deliberately does not offer: private accounts, per-post audience controls, group chats, blocking or
muting other users, bookmarks, notification preferences, dark mode, and a settings page. See KB-005 and KB-059.

Related: KB-001, KB-005, KB-033, KB-054

## KB-003 — Accounts and identity: username, display name and handle
Applies to: Accounts, Profile

Every FOMO account carries three pieces of identity, and users routinely confuse them.

| Field | What it is | Rules |
|---|---|---|
| Username | Your unique handle, shown as @yourname throughout the site | 3–100 characters, must be unique across the whole platform |
| Display name | The friendly name shown in large type on your profile and above your posts | Up to 150 characters, need not be unique, can be blank |
| Email address | Used to sign in and to receive your verification code | Must be unique; never shown to other users |

Your username is what other people search for — FOMO's people search matches usernames only, not display
names (KB-043). If a user complains that nobody can find them, the usual cause is that they set a display name
but left the username as the one generated at sign-up.

Both the username and the display name can be changed at any time from the Edit profile screen (KB-020). The
email address cannot be changed by the user.

Related: KB-008, KB-020, KB-043

## KB-004 — Follows and friends: the difference
Applies to: Connections, Platform overview

FOMO has two separate relationship systems, and they behave differently. This is the single most common source
of confusion in support tickets.

| | Following | Friendship |
|---|---|---|
| Direction | One-way | Mutual |
| Approval | None — instant | The other person must accept |
| How it starts | Press Follow | Send a friend request, they accept |
| How it ends | Press Unfollow | Press Unfriend |
| Effect | Their posts appear in your Following feed | You appear in each other's friends list |
| Can be refused? | No | Yes — requests can be rejected |

Three consequences worth knowing:

1. Following someone does not make you friends, and being friends is not required to follow.
2. Accepting a friend request automatically makes both people follow each other. This is deliberate: friends
   should see each other's posts.
3. Unfriending does not unfollow. After you unfriend someone you are still following them, and they are still
   following you, until one of you also presses Unfollow.

Neither relationship is required to send someone a private message — anyone can message anyone (KB-045).

Related: KB-034, KB-038, KB-042, KB-045

## KB-005 — What is public and what is private on FOMO
Applies to: Privacy, Posts, Profile

Short answer: almost everything except your private messages is public.

Public — visible to anyone, including people who are not signed in:
- Your profile: display name, username, bio, profile photo, cover photo
- Your follower, following and friend counts, and the lists themselves
- Every post you have published, including its likes, comments and share count
- Your comments and replies on other people's posts

Private — visible only to you:
- Your archived posts (KB-028)
- Your private conversations and their attachments
- Your notifications
- Your email address

There are no privacy settings. FOMO has no private-account option, no per-post audience selector, and no
"friends only" visibility. When a user asks how to make their account private or restrict a post to friends, the
honest answer is that the platform does not support it — the only way to take content out of public view is to
archive it or delete it.

Likewise there is no way to block, mute or restrict another user. A user who is being harassed should be
directed to an administrator (KB-082).

Related: KB-028, KB-057, KB-082

## KB-006 — How FOMO works behind the scenes
Applies to: Platform overview, Troubleshooting background

You do not need this to answer most questions, but several common failures only make sense once you know
which component is responsible.

FOMO is made of five parts:

1. The website — what runs in the user's browser. It draws every screen and holds nothing permanently;
   everything it shows it has just fetched.
2. The API — the service the website talks to. It holds all the rules: who may edit what, how long a code lasts,
   how big a file may be.
3. The database — where accounts, posts, comments, relationships and messages live.
4. File storage — a separate cloud storage service holding every uploaded photo, video and document. Images
   are stored exactly as uploaded; nothing is resized or compressed.
5. The email sender — a standard mail service used for exactly one thing: sending the 6-digit verification code
   at sign-up. FOMO sends no other email, ever.

Live chat uses a persistent connection held open between the browser and the API for as long as the conversation
screen is open. This is what makes messages appear instantly. If that connection drops, the chat screen falls back
to checking for new messages every few seconds, so conversations keep working — just with a short delay
(KB-053).

What this explains in practice:
- A verification email that never arrives is a mail-service problem, not an account problem (KB-060).
- An upload that fails while the rest of the site works fine points at file storage.
- "Offline" on the chat screen means the persistent connection dropped, not that the other person is offline (KB-053).
- Notifications are not delivered over the live connection — only chat is. That is why notifications take up to a minute to appear (KB-058).

Related: KB-053, KB-058, KB-060, KB-071

## KB-007 — Creating an account
Applies to: Sign-up

Steps

1. Go to Create account from the login screen.
2. Fill in Full name, Email address, Password and Confirm password.
3. Press Create account.
4. A green banner confirms: "Account created! Check your email for the verification code."
5. After about two seconds you are moved automatically to the verification screen, with your email address already filled in.
6. Enter the 6-digit code from your email (KB-009).
7. You are returned to the login screen and can now sign in (KB-011).

Rules

- The email address must not already be registered, and the derived username must be free. If either is taken you get: "A user with this email or username already exists."
- The password must be at least 8 characters. There is no requirement for capitals, digits or symbols.
- Full name must be at least 2 characters.
- You cannot sign in until you have verified your email. An unverified account exists but is locked; attempting to sign in returns "Please verify your email before logging in" (KB-062).

Support note. The Create account screen shows Google and GitHub buttons, but on that screen they are
decorative and do nothing. Social sign-in works only from the login screen (KB-012).

Important behaviour worth knowing: account creation and the verification email are a single transaction. If the
email cannot be sent, the account is not created — it is removed again and you get "Could not send verification
email. Please try registering again." So a user who reports "I registered but got no email and now it says my
email is already taken" has actually got two different problems; see KB-060.

Related: KB-008, KB-009, KB-060, KB-062

## KB-008 — How your username is chosen
Applies to: Sign-up, Profile, Identity

You are never asked for a username at sign-up. FOMO derives one for you:

- Registering with email and password: your username is the first word of your full name, in lower case. Entering "Priya Sharma" produces the username priya.
- Registering through Google or GitHub: your username comes from the part of your email address before the @. If that is already taken, a six-character random suffix is added — for example jane_a1b2c3.

This surprises people, and it is a frequent ticket: users expect their handle to match their full name and find they
are @priya rather than @priyasharma.

You can change it. Go to your profile, press Edit profile, and edit the Username field. It must be 3–100
characters and unique; if someone else has it you get "That username is already taken."

Related: KB-003, KB-020

## KB-009 — The 6-digit verification code
Applies to: Sign-up, Email verification

After you register, FOMO emails a 6-digit numeric code to the address you signed up with. Entering it correctly
is what activates your account.

The rules

| | |
|---|---|
| Length | 6 digits, numbers only |
| Valid for | 10 minutes from the moment it was sent |
| Attempts allowed | 5 |
| Codes active at once | 1 — requesting a new code cancels the previous one |

The verification screen has six single-digit boxes. They advance automatically as you type, backspace moves you
back a box, and you can paste all six digits at once.

What the failures mean

- "Invalid OTP. N attempts remaining." — wrong code; the count tells you how many tries are left.
- "OTP has expired. Please request a new one." — more than 10 minutes have passed.
- "Too many failed attempts. Please request a new OTP." — you used all 5 tries. The code is dead; press Resend code.
- "No OTP found. Please request a new one." — there is no active code for this address.

Support note. The verification screen says "Code expires in 15 minutes". The code actually stops working after
10 minutes. Answer users based on 10 minutes; if they insist the screen said 15, they are reading it correctly and
the wording is simply wrong.

Support note. If a user has requested several codes, only the most recent one works. Users often try the first
email they received and are told the code is invalid.

Related: KB-010, KB-060, KB-064, KB-065

## KB-010 — Resending the verification code
Applies to: Sign-up, Email verification

On the verification screen, Resend code is greyed out for the first 60 seconds and shows a countdown ("Resend in
43s"). Once it becomes available you can press it as often as you like — there is no daily cap.

Each resend cancels the previous code. Always tell the user to use the newest email.

Success shows "New code sent to your email!". Failure shows "Failed to resend code", which almost always
means the mail service is temporarily unavailable — try again in a few minutes.

If a user has closed the verification screen, there is no link back to it from anywhere in the app — attempting to
sign in only tells them the account is unverified. To get a fresh code they need to return to the verification address
directly: /verify-email?email=<their email address>. Support can send them that link.

Related: KB-009, KB-060

## KB-011 — Signing in with email and password
Applies to: Sign-in

Go to Log in, enter your email address and password, and press Log in. The eye icon beside the password field
reveals what you have typed. On success you land on your feed.

Why a sign-in can fail

| Message | Meaning |
|---|---|
| Invalid email or password | Wrong address or wrong password — the message is deliberately vague and does not tell you which |
| Please verify your email before logging in | The account exists but was never verified (KB-062) |
| This account is blocked | An administrator has blocked the account (KB-063) |
| This account is deleted | The account was removed by an administrator |
| HTTP 429 / too many requests | More than 20 sign-in attempts a minute from your network (KB-067) |

There is no password reset. If the password is genuinely forgotten, the user cannot recover the account
themselves — see KB-017.

Related: KB-012, KB-017, KB-061, KB-062, KB-063

## KB-012 — Signing in with Google or GitHub
Applies to: Sign-in, Social sign-in

The login screen offers Google and GitHub buttons above the email fields. Pressing one sends you to that
provider, and after you approve the request you are returned to FOMO already signed in, via a brief "Completing
sign in…" screen.

Things worth knowing

- Social accounts skip email verification entirely. The provider has already confirmed the address, so there is no 6-digit code.
- If the email already has a FOMO account, the provider is linked to it rather than creating a duplicate. Signing up with a password and later using Google with the same address gets you into the same account.
- You can link both Google and GitHub to one account.
- Your username is derived from your email address (KB-008).

When it does not work

- "Google OAuth not configured yet" / "GitHub OAuth not configured yet" — social sign-in has not been set up on this deployment. Use email and password instead.
- "GitHub account has no accessible email address." — GitHub is not sharing an address. The user must make an email public or verified in their GitHub settings, then retry.
- Returning to the login screen with an oauth_failed error usually means the sign-in was abandoned or took too long. Simply try again.

Support note. The Google and GitHub buttons on the Create account screen do nothing. Social sign-in must be
started from the login screen — and it creates the account for you on first use, so there is no need to register first.

Related: KB-013, KB-007, KB-011

## KB-013 — Why a social sign-in account has no password
Applies to: Sign-in, Social sign-in

An account created through Google or GitHub has no password at all. It was never asked for one.

The practical consequences:

- That account cannot sign in with the email-and-password form. Attempting it returns "Invalid email or password", which is misleading — the account exists and is fine, it simply has no password to check.
- There is no way to add a password later. FOMO has no "set a password" screen.
- The user must always sign in with the same provider button they originally used.

This produces a recognisable ticket: "I can log in with Google but not with my email and password, even though
it's the same account." That is expected behaviour. Direct the user to the Google or GitHub button.

If the user has lost access to the provider account itself, the FOMO account is effectively unreachable and the case
has to go to an administrator (KB-082).

Related: KB-012, KB-017, KB-061, KB-082

## KB-014 — Why you get signed out, and how long a session lasts
Applies to: Sessions, Sign-in

FOMO holds your session in two parts:

- A short-lived pass valid for 15 minutes, used for each request.
- A long-lived pass valid for 7 days, used only to silently issue a new short-lived one.

In normal use this is invisible. Every 15 minutes the site quietly renews itself in the background. You stay signed
in for up to 7 days of continuous use, and each renewal extends the window — so an active user is rarely signed
out at all.

You will be signed out when:

- You have not used FOMO for more than 7 days.
- You pressed Logout.
- An administrator blocked or deleted your account — this takes effect immediately, even mid-session (KB-063).
- Your browser is discarding cookies (see KB-066), which is by far the most common cause of complaints about repeated sign-outs.

Your session lives in secure browser cookies that JavaScript cannot read. There is no token to copy, no "stay
signed in" tickbox, and no way to see or end sessions on other devices.

Related: KB-015, KB-016, KB-066, KB-063

## KB-015 — Using FOMO on more than one device
Applies to: Sessions

You can be signed in on as many devices and browsers as you like at the same time — a laptop, a phone and a
tablet all work simultaneously. Signing in somewhere new does not sign you out anywhere else.

Live chat is aware of this: if you have the same conversation open in two places, a new message appears in both
at once.

Limitations to be aware of

- There is no "signed-in devices" screen, so a user cannot see where they are logged in and cannot remotely sign out a device they no longer have.
- Pressing Logout ends the session only on the device you pressed it on.
- If a user believes someone else has access to their account, they cannot change their password (there is no such feature) and cannot revoke other sessions. The only remedy is an administrator blocking and then unblocking the account, which ends every session everywhere — see KB-082.

Related: KB-014, KB-016, KB-082

## KB-016 — Signing out
Applies to: Sessions

Press Logout at the top right of the navigation bar. You are returned to the login screen immediately.

Logging out clears your session cookies and invalidates the long-lived pass on that device, so the browser cannot
silently sign itself back in. It has no effect on any other device (KB-015).

Logging out never fails: even if the session had already expired, the cookies are cleared and you end up on the
login screen.

Related: KB-014, KB-015

## KB-017 — I forgot my password
Applies to: Sign-in, Account recovery

FOMO has no password reset. There is no "forgot password" flow, no reset email, and no way for a user to
change their own password from inside the app.

Support note. The login screen shows a Forgot password? link. It leads to a page that does not exist and the user
gets a "page not found" error. Warn users before they press it.

What to do instead

1. Check first whether the account was created with Google or GitHub. If so there is no password to recover and never was — the user simply needs to press the right button (KB-013). This resolves a large share of these tickets.
2. If it is a genuine email-and-password account, the user cannot get back in unaided. The case must be escalated to an administrator (KB-082).
3. If the user still has access to the email address but nothing else, there is no self-service path — the email address alone does not unlock anything, because no reset email exists to send.

Do not advise the user to register again with the same email address. It will be rejected as already taken, and it
does not release the original account.

Related: KB-013, KB-061, KB-082

## KB-018 — Account statuses: active, blocked, suspended, deleted
Applies to: Accounts, Moderation

Every FOMO account is in exactly one of four states. Only administrators can change them.

| Status | What it means | What the user experiences |
|---|---|---|
| Active | Normal | Everything works |
| Blocked | An administrator has withdrawn access | Cannot sign in; "This account is blocked". Any open session stops working immediately |
| Suspended | A restricted state | Same as blocked in practice — cannot sign in or use the site |
| Deleted | The account has been removed | Cannot sign in; disappears from search and from public listings |

Three points that matter for support:

- Blocking is immediate and total. A user who is blocked while browsing does not stay signed in until their session expires; the very next thing they click fails.
- Deletion is reversible from the inside. A deleted account is marked as deleted rather than erased — its posts and messages still exist in the system and an administrator can still see the record. It is invisible to other users, however.
- Unblocking restores access, but the user must sign in again — all their sessions were ended when they were blocked.

Related: KB-063, KB-077, KB-078

## KB-019 — Your profile page
Applies to: Profile

Your profile is reached from Profile in the navigation bar, or by clicking your avatar at the top right. Other
people's profiles open when you click their name or avatar anywhere on the site.

A profile shows:
- A cover photo banner across the top (a purple gradient if none is set)
- A circular profile photo, or an automatically generated initials image if none is set
- Display name, @username and bio
- Four counts: posts, followers, following and friends
- Every post that person has published, newest first

The follower, following and friend counts are clickable and open a list you can act from (KB-037). The post count
is not clickable.

On your own profile you also get an Edit profile button and a "…" menu containing View archived posts.

On someone else's profile you get Follow/Unfollow, a friend button whose label changes with the state of your
relationship, and Message.

Archived and deleted posts never appear on a profile anyone else is viewing (KB-028).

Related: KB-020, KB-028, KB-037

## KB-020 — Editing your display name, username and bio
Applies to: Profile

Go to your profile and press Edit profile. The dialog lets you change:

| Field | Limit | Notes |
|---|---|---|
| Username | 3–100 characters | Must be unique across the platform |
| Name (display name) | 150 characters | Can be left blank; need not be unique |
| Bio | 500 characters | Free text |

Press Save to apply, Cancel to discard. Changes appear immediately on your profile and in the navigation bar.

Errors you may see

- "Username cannot be empty" — the username field was cleared. It is required.
- "That username is already taken" — pick a different one.
- "Failed to save profile" — a network or server problem; try again.

Changing your username is safe. Posts, comments, followers, friends and conversations all stay attached to your
account. But note that anyone who bookmarked your old handle will not find you, and people search matches
usernames only (KB-043).

Related: KB-003, KB-008, KB-021, KB-043

## KB-021 — Changing your profile photo and cover photo
Applies to: Profile, Media

Both are changed from the same place: profile → Edit profile.

- Profile photo (avatar): hover the circular photo and press the camera icon.
- Cover photo: press Change cover on the banner strip.

Pick a file, check the live preview, then press Save. Nothing is applied until you save.

Limits

| | Maximum size | Accepted formats |
|---|---|---|
| Profile photo | 5 MB | JPEG, PNG, WebP, GIF |
| Cover photo | 8 MB | JPEG, PNG, WebP, GIF |

Videos and documents are rejected for both.

If a file is too big you get "Avatar must be under 5MB" or "Cover photo must be under 8MB" before anything is
uploaded.

Images are stored exactly as uploaded. FOMO does not resize, crop or compress them, so a large photo stays
large and may be slow to load for other people. Advise users to upload something reasonably sized rather than a
full-resolution camera image.

Related: KB-022, KB-025, KB-068

## KB-022 — Removing your profile photo or cover photo
Applies to: Profile, Media

The Edit profile dialog offers a Remove control for the cover photo and a small bin icon for the profile photo.

Support note — these controls do not currently work. Pressing either one produces a server error rather than
removing the picture, and the dialog reports a failure to save. This affects every user; it is not specific to any
account or file.

Workaround. A user who wants rid of their current photo should upload a replacement instead. Uploading a
new profile or cover photo works normally and immediately replaces the old one. Suggest a plain or neutral image
if they simply want the picture gone.

If a user specifically needs the photo removed rather than replaced, escalate — the change has to be made for
them.

Related: KB-021, KB-082

## KB-023 — Writing a post
Applies to: Posts

The composer sits at the top of your feed, headed What's on your mind?

1. Type your text — up to 10,000 characters.
2. Optionally press the camera icon to attach one photo or video (KB-025).
3. Press Post.

The post appears immediately at the top of the For You feed and on your profile.

Rules

- A post cannot be empty. It needs at least one character of text.
- One media file per post. There is no multi-image post or gallery.
- Every published post is public — to everyone, including people who are not signed in. There is no audience selector (KB-005).
- Text is shown truncated at about 220 characters with a more link; the full text is always there.

Hashtags work by simply typing #word in the text. There is no separate tag field. Tags used in recent posts show
up in Trending Topics on the Explore screen (KB-043).

If posting fails you get "Failed to create post". This is usually a connection problem — retry.

Related: KB-024, KB-025, KB-070, KB-005

## KB-024 — Character limits across FOMO
Applies to: Posts, Comments, Messaging, Profile

Every text field on the platform and its maximum length:

| Where | Limit |
|---|---|
| Post | 10,000 characters |
| Caption when sharing a post | 10,000 characters |
| Comment or reply | 2,000 characters |
| Private message | 5,000 characters |
| Bio | 500 characters |
| Display name | 150 characters |
| Username | 100 characters (minimum 3) |
| Emoji reaction | 16 characters |

Minimums matter too: posts, comments and messages must each contain at least one character. A message is the
one exception — it may be empty if it carries an attachment (KB-047).

If a limit is exceeded the request is rejected with a field-level validation error rather than a friendly message. In
practice the interface stops you first, since each field caps what you can type.

Related: KB-023, KB-032, KB-046

## KB-025 — Adding a photo or video to a post
Applies to: Posts, Media

Press the camera icon in the composer, choose a file, and you get an inline preview with an ✕ to remove it before
posting.

Accepted formats: JPEG, PNG, WebP, GIF and MP4 video. No other video format is accepted — not MOV, not
AVI, not WebM. A user with a phone video will often need to convert it.

Size limits: the composer refuses images over 5 MB and videos over 25 MB.

Support note. The 5 MB image cap is imposed by the composer only; the server itself would accept an image up
to 25 MB. In practice the composer's limit is what users hit, so answer with 5 MB for images and 25 MB for
video. There is no way to bypass the composer's check.

One important behaviour: the post is created first and the file is attached afterwards. If the upload fails, the post
is still published — just without the picture. The message is "Post created, but the attachment failed to
upload". See KB-070 for how to fix it.

Related: KB-021, KB-068, KB-070

## KB-026 — Editing a post
Applies to: Posts

Open the "…" menu on your own post and choose Edit. The post turns into a text box; make your changes and
press Save, or Cancel to abandon them.

Only the author can edit a post. The menu does not appear on anyone else's posts.

You can edit the text only. The attached photo or video cannot be changed or removed after posting — to
change the media you must delete the post and create a new one.

There is no edit history and no "edited" marker on posts. Nobody can tell a post was changed. (Private
messages do show an "edited" marker — see KB-048.)

There is no time limit; a post can be edited years later.

Administrators can also edit any post (KB-079).

Related: KB-027, KB-048, KB-079

## KB-027 — Deleting a post
Applies to: Posts

Open the "…" menu on your own post and choose Delete. A confirmation appears: "Delete this post? This cannot
be undone."

Once deleted:
- The post disappears from your profile, from everyone's feed, and from search
- Its comments and likes go with it
- Your post count drops by one
- It cannot be restored by you or by support

If someone had shared your post, their share remains, but the quoted copy of your post inside it goes blank and
shows "Original post unavailable" (KB-030).

If the user only wants the post out of sight, archiving is the better answer — it is reversible and takes the post
out of public view just as effectively (KB-028).

Related: KB-028, KB-030, KB-079

## KB-028 — Archiving a post, and how it differs from deleting
Applies to: Posts

Archiving hides a post from everyone except you, without destroying it.

Open the "…" menu on your own post and choose Archive. The post immediately leaves your profile and
everyone's feed.

| | Archive | Delete |
|---|---|---|
| Reversible | Yes — unarchive any time | No |
| Visible to others | No | No |
| Visible to you | Yes, in Archived posts | No |
| Counts toward your post count | No | No |
| Can be shared by others | No | No |

Other details worth knowing:

- If someone opens a direct link to your archived post, they get "post not found" rather than a message saying it is archived. This is deliberate — the existence of the post is not disclosed.
- Archived posts cannot be shared; attempting it returns "Archived posts can't be shared".
- If someone shared your post and you then archive the original, the quoted copy inside their share goes blank.
- Your own archived posts still appear when you view your own profile, marked with a grey Archived chip.

Related: KB-027, KB-029, KB-030

## KB-029 — Finding and restoring archived posts
Applies to: Posts

Go to your profile, open the "…" menu beside Edit profile, and choose View archived posts. A dialog lists
everything you have archived.

From that dialog you can:
- Unarchive a post — it returns to your profile and to the public feed immediately, at its original position by date, not at the top
- Delete it permanently

If you have never archived anything the dialog says: "Nothing archived yet. Archived posts are hidden from your
profile grid but stay here until you unarchive or delete them."

There is no time limit — archived posts stay archived indefinitely and are never automatically removed.

Related: KB-028, KB-027

## KB-030 — Sharing (reposting) someone's post
Applies to: Posts, Sharing

Press Share on any post. A dialog opens with an optional caption box and a preview of the post you are sharing.
Press Share to publish.

The result is a new post of your own that quotes the original, showing the original author's name and text. It
appears at the top of the feed and on your profile like any other post, and can itself be liked, commented on and
shared.

Points that generate tickets

- Your caption is optional. Without one, the share is just the quoted original.
- Sharing increases the share count on the original post.
- The original author is not notified that you shared their post. There is no share notification of any kind (KB-057).
- Archived posts cannot be shared — you get "Archived posts can't be shared" (KB-028).
- If the original post is later deleted or archived, your share survives, but the quoted block inside it becomes the italic text "Original post unavailable". Nothing is broken; the source content is simply gone. There is no way to recover it.
- You can delete your own share at any time; that has no effect on the original.

Related: KB-027, KB-028, KB-057

## KB-031 — Liking a post
Applies to: Posts, Likes

Press the heart on any post. It fills in red and the count rises. Press it again to remove the like — it is a simple
toggle, and there is only one kind of reaction on posts (emoji reactions exist in private messages only, KB-050).

- You can like your own posts. Doing so notifies nobody.
- Liking someone else's post sends them a notification (KB-055).
- There is no list of who liked a post — only the count.
- Counts above a thousand are abbreviated, so 1,800 shows as "1.8K".
- The heart responds instantly, before the server has confirmed. If the request then fails, the heart quietly reverts to its previous state. A user reporting that "my like doesn't stick" is seeing a connection problem — ask them to reload and try again.

Related: KB-032, KB-050, KB-055

## KB-032 — Comments and replies
Applies to: Comments

Press Comment on a post to open the thread beneath it. Type in the Write a comment… box and press Send.

- Comments are up to 2,000 characters
- The whole thread loads at once, oldest first — there is no pagination
- Press Reply under a comment to answer it. Replies are shown indented beneath their parent
- Threading is one level deep: you can reply to a comment, but not to a reply
- Empty threads show "No comments yet. Be the first to comment."

Who can delete a comment

Two people can delete any given comment: the person who wrote it, and the author of the post it is on. That
means a post author can moderate their own comment section, which is the closest thing FOMO has to a userlevel moderation tool.

Deleting a comment also removes its replies, and reduces the post's comment count. The count shown on a post
includes replies as well as top-level comments.

Comments cannot be edited. To change a comment you must delete it and write a new one.

Comments cannot be liked. A like count exists on the display but is always zero and there is no control to set it.

Related: KB-024, KB-031, KB-055

## KB-033 — Saving or bookmarking posts
Applies to: Posts

FOMO has no bookmarking, saving or "read later" feature. There is no way to keep a private list of posts.

The workarounds available to a user are:

- Like the post. This is public, but likes are at least retrievable in the sense that the post stays associated with you.
- Share the post to your own profile, optionally with a caption noting why you kept it. This is public.
- Copy the link from the browser address bar and keep it in a browser bookmark. Note that FOMO has no individual post page, so a link to a post is not something the platform produces — the practical unit is a link to the author's profile.

If a user reports that the save icon "does nothing", they are correct: no such control is offered.

Related: KB-031, KB-030

## KB-034 — Following someone
Applies to: Connections, Following

Following is one-way and instant. Nobody has to approve it and there are no private accounts to request access to.

Where you can follow someone

- On their profile — the Follow button in the header
- On the Explore screen, from a Featured Creator card or a people-search result
- Inside the Followers / Following / Friends list dialog, from any row
- On a "started following you" notification, using the inline Follow button

The button changes to Following immediately. From then on their posts appear in your Following feed (KB-036),
and they receive a notification that you followed them.

Rules

- You cannot follow yourself.
- Following someone twice does nothing — the button already shows Following.
- The person you follow is not asked and cannot decline. If they do not want you following them, FOMO offers them no remedy: there is no block or remove-follower feature (KB-005).

Related: KB-004, KB-035, KB-036, KB-043

## KB-035 — Unfollowing someone
Applies to: Connections, Following

Press Following on their profile — or in any list where the button appears — and it reverts to Follow. The change
takes effect at once.

- Their posts disappear from your Following feed straight away.
- They are not notified that you unfollowed them.
- Your following count and their follower count both drop by one.
- You can follow them again at any time.
- Unfollowing and unfriending are separate actions. If you are friends with someone and you unfollow them, you remain friends — you just stop seeing their posts in the Following feed. Equally, unfriending does not unfollow (KB-042).

Related: KB-034, KB-042, KB-004

## KB-036 — The Following feed and why it may be empty
Applies to: Feed

The feed has two tabs:

- For You — every public post on the platform, newest first
- Following — posts only from accounts you follow

The Following tab shows exactly three things and nothing else: active posts, from people you follow, newest
first.

Which explains the four most common complaints:

| "Why is…" | Because |
|---|---|
| …my Following feed empty? | You are not following anyone yet. It does not fall back to showing popular posts — it is genuinely empty until you follow someone. Use Explore (KB-043) |
| …my own post not in my Following feed? | The Following feed deliberately excludes your own posts. They are on your profile and in For You |
| …someone's post missing? | They archived or deleted it, or you unfollowed them |
| …it not sorted by popularity? | There is no ranking algorithm anywhere on FOMO. Both tabs are strictly newest-first |

Both tabs load 20 posts at a time. Scrolling loads more automatically, and there is also a Load more button. When
you reach the end you get "You're all caught up".

Related: KB-034, KB-043, KB-005

## KB-037 — The Followers, Following and Friends lists
Applies to: Connections

On any profile, the followers, following and friends counts are clickable. All three open the same dialog, which
has a tab for each — so you can switch between them without going back.

Each row shows a person's photo, display name and @handle, and lets you act on them directly:

- Follow / Following toggle
- A small person-plus icon to send a friend request. Once sent it becomes an amber clock icon meaning "Pending — click to cancel"
- A green Friends chip if you are already friends, which changes to Unfriend when you hover over it, with a confirmation
- Clicking a row opens that person's profile.

The list loads 20 people at a time and fetches more as you scroll. The counts in the tab headers are live and update
as you act.

Empty lists say "No followers yet.", "No following yet." or "No friends yet."

If the dialog shows "Something went wrong loading this list.", close it and reopen it; this is a transient loading
failure.

Related: KB-034, KB-038, KB-042

## KB-038 — Sending a friend request
Applies to: Connections, Friends

Friendship is mutual and must be accepted. To ask:

- Open the person's profile and press Add friend, or
- Press the person-plus icon on their row in any Followers / Following / Friends list

The button changes to Cancel request and they receive a friend-request notification.

Rules and the errors they produce

| Situation | Message |
|---|---|
| Sending to yourself | You cannot send a friend request to yourself |
| A request already pending in either direction | A pending friend request already exists between you two |
| You are already friends | You are already friends with this user |

That second rule catches people out. If they already sent you a request, you cannot send one back — you have to
go to your notifications and accept theirs instead (KB-040).

A request you have sent stays pending until they act on it. There is no expiry. You can see everything you have
sent, and cancel it, on the Friends screen (KB-041).

Related: KB-039, KB-040, KB-041, KB-004

## KB-039 — Accepting or rejecting a friend request
Applies to: Connections, Friends

Incoming friend requests appear in your Notifications (KB-040), each with Accept and Reject buttons directly on
the notification.

If you accept:
- You become friends immediately, and appear in each other's friends lists
- You automatically follow each other. This is deliberate, so friends see each other's posts. If you were already following, nothing is duplicated
- The person who sent the request is notified that you accepted

If you reject:
- The request disappears
- The sender is not told. Rejections are silent by design — from their side the request simply stays pendinglooking until they check their Friends screen and find it gone
- They can send a new request later; rejection is not permanent

Only the recipient can accept or reject. If you press a button and see the neutral message "Already resolved", the
request was actioned somewhere else — usually in another browser tab, or by the sender cancelling it.

Related: KB-038, KB-040, KB-041, KB-004

## KB-040 — Where incoming friend requests appear
Applies to: Connections, Friends, Navigation

Incoming friend requests appear under Notifications, not under Friends.

This is the single most common navigation complaint on the platform. Users go to the Friends screen expecting
to find requests waiting for them, see only their own sent requests and their friends list, and conclude that the
request was never delivered.

- Notifications — friend requests you have received, with Accept and Reject buttons
- Friends — friend requests you have sent (with a Cancel button), and your existing friends

The Friends screen itself carries a pointer saying "Incoming friend requests now show up under Notifications."

Note also that the Friends screen is not linked from the navigation bar. It is reached by going to /friends
directly, or by following a link from elsewhere in the app. Users frequently cannot find it at all.

Related: KB-039, KB-041, KB-056

## KB-041 — Cancelling a friend request you sent
Applies to: Connections, Friends

Two ways:

- Go to the Friends screen. Requests you have sent are listed under Sent requests, each with a Cancel button.
- On the person's profile, the button will read Cancel request — press it.
- In a Followers / Following / Friends list, press the amber clock icon on their row.

Cancelling removes the request completely. The other person is not told, and if they had not yet looked at their
notifications they will never know it existed.

You can send a fresh request afterwards at any time.

Only the sender can cancel. If the recipient has already accepted or rejected it in the meantime, cancelling fails
with "This friend request has already been resolved" — reload the screen to see the current state.

Related: KB-038, KB-039, KB-040

## KB-042 — Unfriending someone
Applies to: Connections, Friends

Two ways:

- On their profile, hover the green Friends button — it changes to Unfriend
- On the Friends screen, press Unfriend on their row

You are asked to confirm: "Unfriend <name>? You can send a new friend request later."

What happens

- The friendship ends for both of you, immediately and symmetrically
- You do not stop following each other. This surprises almost everyone. Accepting a friend request made you follow each other (KB-039); unfriending does not undo that. Their posts keep appearing in your Following feed until you also press Unfollow (KB-035)
- The other person is not notified
- Either of you can send a new friend request afterwards

If a user wants a clean break, tell them to do both: unfriend and unfollow. And note that neither prevents the other
person from following them back or messaging them — FOMO has no blocking (KB-005).

Related: KB-035, KB-039, KB-004, KB-005

## KB-043 — Finding people and content on FOMO
Applies to: Discovery, Search

The Explore screen is the discovery surface. It has a search box and four tabs.

Search — people only. Typing in the box searches as you type and matches usernames only. It does not search
display names, bios or post text. Someone searching for "Priya Sharma" will not find @priya unless they type
"priya".

The four tabs

| Tab | What it does |
|---|---|
| All | Trending Topics and Featured Creators |
| People | Live username search with Follow buttons |
| Posts | Not available — "Searching posts by keyword is coming soon." |
| Tags | Not available — "Browsing all hashtags is coming soon." |

Trending Topics are hashtags drawn from recent posts, shown as chips with a post count. They are calculated
from the most recent few hundred posts, so this is a snapshot of what is current rather than an all-time ranking. A
tag that was busy last month will not appear.

Featured Creators is simply the accounts with the most followers. It is not personalised and is the same for
everyone.

There is no content search. Users cannot search post text, hashtags cannot be clicked through to a list of posts,
and there is no way to find an old post except by scrolling the author's profile. This is a frequent and legitimate
complaint; the answer is that the feature has not been built.

Related: KB-003, KB-034, KB-036

## KB-044 — Starting a conversation
Applies to: Messaging

There are three ways to open a chat with someone:

- On their profile, press Message
- On the Friends screen, press Message on their row
- On the Messages screen, click an existing conversation

All three land you on the conversation screen.

You only ever have one conversation with a given person. Pressing Message a second time reopens the same
thread with all its history — it never creates a duplicate.

You cannot start a conversation with yourself; the attempt returns "You cannot start a conversation with
yourself".

The Messages screen lists every conversation you have, sorted by the most recent message, each showing the
other person's photo and name, a preview of the last message, a relative timestamp, and an unread badge. The
search box on that screen filters your existing conversations by name or message text — it does not search for
new people.

Empty state: "No conversations yet. Message a friend to get started."

Related: KB-045, KB-046, KB-052

## KB-045 — Who you can message
Applies to: Messaging, Privacy

Anyone. You do not need to be friends, and neither of you needs to follow the other. Any account can message
any other account.

There is no message-request inbox, no filtering of messages from strangers, and no way to prevent someone from
messaging you. FOMO has no block or mute feature (KB-005).

This is worth stating plainly, because it produces a specific and serious kind of ticket: a user receiving unwanted
messages has no self-service remedy. The options are:

1. Ignore the conversation — it stays in the list but does nothing on its own
2. Delete the offending messages — not possible; you can only delete your own messages (KB-049)
3. Escalate to an administrator, who can block the offending account (KB-082)

There is also no way to delete or leave a conversation. Once a thread exists it stays on your Messages screen
permanently.

Related: KB-044, KB-049, KB-005, KB-082

## KB-046 — Sending a message
Applies to: Messaging

Type in the Message… box at the bottom of the conversation and press the send arrow.

- Messages are up to 5,000 characters
- A message must have text or an attachment. Sending nothing returns "Message must have content or an attachment"
- Messages appear instantly for both people when the live connection is up (KB-053)
- Your own messages appear on the right in indigo; the other person's on the left in grey with their photo
- The thread loads 50 messages at a time, oldest first, and scrolls automatically to the newest message.

If sending fails you see "Failed to send message." — the message was not delivered and you should try again.
This is normally a connection problem.

Empty conversation: "No messages yet. Say hello!"

Related: KB-047, KB-051, KB-053, KB-072

## KB-047 — Sending photos, videos and files in chat
Applies to: Messaging, Media

Press the + button beside the message box and choose a file. It appears as a chip above the composer with an ✕ to
remove it, and an "Uploading… 42%" progress line while it transfers. Send the message to deliver it.

Chat accepts more file types than posts do:

| Type | Formats |
|---|---|
| Images | JPEG, PNG, WebP, GIF |
| Video | MP4 only |
| Documents | PDF, DOC, DOCX, TXT |

Maximum size: 25 MB for any chat attachment.

Received attachments display as an inline image, an inline video player, or a downloadable chip showing the file
name and size.

You may send an attachment with no text — that is the one case where an empty message is allowed.

If the upload fails you get "Failed to upload attachment." The file was not sent; the message is not delivered
either. Retry, and if it keeps failing check the file size and format against the table above.

Related: KB-046, KB-068, KB-069

## KB-048 — Editing a message
Applies to: Messaging

Open the "…" menu on one of your own messages and choose Edit. The bubble becomes a text box; change it
and press Save.

- Only the sender can edit a message. The menu does not appear on the other person's messages
- Edited messages are marked "· edited" beside the timestamp, so the other person can tell
- The other person sees the change immediately
- There is no time limit and no version history

This differs from posts, which can be edited without any visible marker (KB-026).

Related: KB-049, KB-026

## KB-049 — Deleting a message
Applies to: Messaging

Open the "…" menu on one of your own messages and choose Delete. Confirm at "Delete this message? This
cannot be undone."

- The message is removed for both people. This is a true delete, not a hide — the other person's copy disappears too, along with any reactions on it
- It cannot be recovered
- If it was the most recent message, the conversation preview on the Messages screen falls back to the message before it
- You can only delete messages you sent. There is no way to remove something someone else sent you (KB-045)

There is no way to delete a whole conversation or clear its history — only messages one at a time, and only your
own.

Related: KB-045, KB-048

## KB-050 — Reacting to a message with an emoji
Applies to: Messaging

Press the emoji button beside any message to open the picker. The available reactions are:

- Either person can react to any message, including their own
- Each emoji is a separate toggle. Pressing the same emoji again removes your reaction. Pressing a different one adds it alongside — it does not replace the first, so one person can put several emoji on the same message
- Reactions appear as pills under the message showing the emoji and a count, highlighted when you are one of the reactors, with a tooltip listing who reacted ("You, Priya")
- Reactions appear for the other person immediately

Emoji reactions exist only in private messages. Posts have a single like and no reactions (KB-031).

Related: KB-031, KB-046

## KB-051 — Read receipts and the tick marks
Applies to: Messaging

Your own messages carry a tick indicator:

| Mark | Meaning |
|---|---|
| ✓ single tick | Sent |
| ✓✓ double tick | Read by the other person |

A message is marked read when the other person opens the conversation. Merely seeing the notification badge
on the Messages tab does not count.

Read receipts cannot be turned off. There is no privacy setting for them, and no way to read a message without the
sender knowing — other than reading the preview text on the Messages list, which does not mark anything read.

Ticks appear only on your own messages; you never see ticks on the other person's messages.

Related: KB-052, KB-046

## KB-052 — Unread message badges
Applies to: Messaging, Notifications

Two badges show unread messages:

- A cyan badge on the Messages tab in the navigation bar — your total across all conversations
- A cyan badge on each row of the Messages screen — that conversation's unread count

Both cap their display at "99+".

How they clear: opening a conversation marks everything in it as read and the badge clears immediately, both on
the row and in the navigation bar.

Your own messages never count toward your own unread badge.

The badges refresh roughly every 20 seconds, whenever you move between screens, and instantly when you read
something. If one looks stale, moving to another screen and back will refresh it. Note that on a network error the
badge deliberately keeps its last known value rather than dropping to zero, so a badge that seems stuck during a
poor connection is behaving as designed.

Related: KB-051, KB-073, KB-056

## KB-053 — The Live / Offline indicator
Applies to: Messaging

The conversation screen shows a small pill at the top reading either Live or Offline.

It describes your own connection to FOMO — not whether the other person is online. This is a persistent
misunderstanding: users see "Offline" and assume the person they are messaging has gone away.

- Live — the persistent connection is up, and messages arrive the instant they are sent
- Offline — that connection has dropped

Offline does not mean chat is broken. When the live connection is down, the screen falls back to checking for
new messages every five seconds, and also checks whenever you switch back to the tab. Messages still send and
still arrive — with a delay of a few seconds instead of being instantaneous. Nothing is lost.

The connection also retries by itself, backing off gradually up to about 15 seconds between attempts, so it usually
recovers on its own.

See KB-071 for what to do when it stays Offline.

Related: KB-071, KB-072, KB-006

## KB-054 — Group chats
Applies to: Messaging

FOMO supports one-to-one conversations only. There are no group chats, and no way to add a third person to
an existing conversation.

There is also no way to broadcast a message to your friends or followers. The nearest equivalent is publishing a
post, which is public (KB-023).

If a user asks how to create a group, the answer is that the feature does not exist. It is not hidden behind a setting
or a permission.

Related: KB-044, KB-023

## KB-055 — The six kinds of notification
Applies to: Notifications

FOMO sends exactly six kinds of notification, and no others:

| Type | Wording | Triggered when |
|---|---|---|
| Like | "<name> liked your recent post" | Someone likes your post |
| Comment | "<name> commented on your post" | Someone comments on your post |
| Reply | "<name> replied to your comment" | Someone replies to your comment |
| Follow | "<name> started following you" | Someone follows you |
| Friend request | "<name> sent you a friend request" | Someone sends you a friend request |
| Friend accepted | "<name> accepted your friend request" | Someone accepts a request you sent |

Each notification shows the other person's photo with a coloured badge indicating the type — a rose heart for
likes, cyan for comments and replies, violet for follows and friend requests, emerald for acceptances. Comment
and post text is quoted in the notification, cut to the first 80 characters.

Some notifications carry an action button you can use without leaving the screen:

- Friend request — Accept and Reject (KB-039)
- Follow — a Follow button to follow them back

You are never notified about your own actions. Liking or commenting on your own post produces nothing.

Related: KB-056, KB-057, KB-039

## KB-056 — Reading and clearing notifications
Applies to: Notifications

Open Notifications from the navigation bar. The list is newest first, 30 at a time.

- Unread notifications are marked with a coloured ring and a cyan dot
- Opening the screen marks everything as read, and the navigation-bar badge clears
- The badge shows your unread count and caps at "99+"

There is no way to delete or clear notifications. There is no "clear all" button, no individual dismiss, and no
archive. The list grows indefinitely; old entries simply fall further down. Reading them is the only state change
available.

Clicking a notification takes you to the relevant place — but note that like, comment and reply notifications
open the other person's profile, not the post. FOMO has no individual post page, so there is nowhere else for
them to go. Users who expect to be taken to the comment they were tagged in will not be; they need to find the
post on their own profile.

Empty state: a bell icon and "You're all caught up."

Related: KB-055, KB-058, KB-073

## KB-057 — What FOMO never notifies you about
Applies to: Notifications

Users often assume a notification was lost when in fact none is ever sent. FOMO produces no notification for any
of the following:

- Someone sharing or reposting your post — the original author is never told
- New private messages — chat has its own unread badge instead (KB-052), and no entry ever appears in the notifications list
- A friend request being rejected — rejections are silent by design (KB-039)
- Someone unfollowing you or unfriending you
- Your own actions — liking or commenting on your own content
- Mentions — there is no @-mention feature at all
- Administrator actions — a user who is blocked or has a post deleted is not told why, or that it happened (KB-077, KB-079)
- Anything by email. FOMO sends exactly one email in its entire lifetime: the 6-digit verification code at signup. There are no email notifications, digests, or security alerts

Related: KB-055, KB-052, KB-059

## KB-058 — Why notifications are not instant
Applies to: Notifications

Notifications are fetched on a schedule, not pushed. The navigation-bar badge refreshes roughly every 20
seconds and whenever you move between screens; the notifications list itself is fetched when you open it.

So a notification can be up to about 20 seconds behind reality, and slightly more if you have left the tab sitting
idle.

This is a deliberate difference from private messages: chat is delivered live over a persistent connection,
notifications are not (KB-006). A user who observes that "messages appear instantly but notifications lag" is
describing the system working as designed.

If a notification seems missing rather than late, check KB-057 first — it may be one of the events that never
generates a notification at all.

Related: KB-006, KB-057, KB-073

## KB-059 — Notification settings and preferences
Applies to: Notifications, Settings

There are no notification settings. FOMO has no settings screen of any kind, and in particular offers no way to:

- Turn any notification type on or off
- Mute a specific person or conversation
- Set quiet hours
- Receive notifications by email — no notification email is ever sent (KB-057)
- Enable browser or push notifications

Every account receives all six notification types (KB-055), always.

The only thing under a user's control is reading them, which clears the badge (KB-056).

Nor is there a settings screen for anything else: no privacy controls, no dark mode, no language selection, no data
export, and no password change. Everything a user can configure lives in the Edit profile dialog (KB-020).

Related: KB-055, KB-056, KB-057, KB-020

## KB-060 — The verification email never arrived
Applies to: Sign-up, Email verification, Troubleshooting

By far the most common ticket on the platform. Work through these in order.

1. Check spam, junk and Promotions. FOMO sends its verification code from an ordinary mail account, not a dedicated bulk-mail service, so filters catch it routinely. This is the cause in most cases. Ask the user to search their whole mailbox for the sender name "Social Media App" or the subject "Your verification code" — note that the sender name is not "FOMO", which is why searching for "FOMO" finds nothing.
2. Wait a minute, then press Resend code. Resend is locked for the first 60 seconds after each send. Remind the user that only the newest code works — if they later find the first email, its code will be rejected (KB-009).
3. Check the address for typos. The verification screen shows the address the code was sent to. If it is wrong, the account is unreachable: the address cannot be changed, and the user must register again with the correct one.
4. Consider that the account may not exist. Account creation and the verification email are a single operation. If the email could not be sent, the account is rolled back and the user sees "Could not send verification email. Please try registering again." If they saw that message, there is no account — they should simply register again.
5. If the address is on a corporate or school domain, the mail may be blocked at the gateway. Ask the user to try a personal address.

Distinguishing the two failure shapes

| What the user reports | What actually happened |
|---|---|
| "It said my account was created but no email came" | The account exists and is unverified. Resend the code |
| "It told me to try registering again" | No account was created. Register again |
| "It says my email is already registered" | An unverified account exists. Send them to /verify-email?email=<address> for a fresh code |

Related: KB-007, KB-009, KB-010, KB-064

## KB-061 — "Invalid email or password"
Applies to: Sign-in, Troubleshooting

The message is deliberately vague and does not say which of the two was wrong. Causes, in rough order of
frequency:

1. The account was created with Google or GitHub. It has no password at all, so the password check can never succeed — even though the account is perfectly healthy. The user must sign in with the provider button they originally used. Check this first: it accounts for a large share of these tickets and there is nothing else to diagnose (KB-013).
2. A genuinely mistyped password. Ask the user to press the eye icon and confirm what they have typed, and to check caps lock.
3. The wrong email address. People frequently register with one address and try to sign in with another.
4. The account does not exist. Registration may have failed at the email step and been rolled back (KB-060).
5. The account was deleted by an administrator. Deleted accounts return their own message, so this is only relevant if the message differs.

If the password is genuinely lost, there is no recovery path — FOMO has no password reset. See KB-017
before promising the user anything.

Related: KB-013, KB-017, KB-060, KB-062

## KB-062 — "Please verify your email before logging in"
Applies to: Sign-in, Email verification, Troubleshooting

The account exists but was never activated with the 6-digit code. Sign-in stays blocked until it is.

Resolution: send the user to the verification screen at /verify-email?email=<their email address>, have
them press Resend code, and enter the new code. They can then sign in normally.

There is no link to that screen from anywhere in the app once the sign-up flow has been left, which is why users
get stuck here — they know they need to verify but cannot find where. Sending them the address directly is the
fastest resolution.

If no email arrives, work through KB-060.

Note that accounts created with Google or GitHub never see this message, as social sign-in skips verification
entirely (KB-012).

Related: KB-009, KB-010, KB-060, KB-012

## KB-063 — "This account is blocked"
Applies to: Sign-in, Moderation, Troubleshooting

An administrator has blocked the account. This is not an error and not something the user can resolve themselves.

What the user experiences

- Sign-in fails with this message
- If they were signed in when it happened, their session stops working immediately — the very next action fails. They are not allowed to continue until their session expires
- Every device is affected at once
- They are not told why, and no email is sent. FOMO has no mechanism for notifying a user of a moderation decision (KB-057)

What support can do

Nothing directly — only an administrator can unblock. Escalate with the account's username or email address. If
the block is reversed, the user must sign in again, since blocking ended all their sessions (KB-077).

A closely related message, "This account is suspended", behaves identically. "This account is deleted" means the
account was removed (KB-078).

Related: KB-018, KB-077, KB-078, KB-082

## KB-064 — The verification code is rejected or has expired
Applies to: Email verification, Troubleshooting

| Message | Cause | Resolution |
|---|---|---|
| Invalid OTP. N attempts remaining. | Wrong digits | Re-read the code; check for a newer email |
| OTP has expired. Please request a new one. | More than 10 minutes since it was sent | Press Resend code |
| Too many failed attempts. | 5 wrong tries used up | Press Resend code (KB-065) |
| No OTP found. Please request a new one. | No active code for this address | Press Resend code |

The two things that cause most of these

1. An old email. Every resend cancels the previous code. If the user has three emails in their inbox, only the newest one works. Tell them to sort by date and use the latest.
2. The 10-minute window. Users often fetch the code, get distracted, and come back too late.

Support note. The screen states "Code expires in 15 minutes". The real limit is 10 minutes. If a user says the
code failed within the stated time, they are not mistaken — answer on the basis of 10 minutes.

The code is always 6 digits, numbers only. If a user reports letters in it, they are reading something else in the
email.

Related: KB-009, KB-010, KB-060, KB-065

## KB-065 — "Too many failed attempts. Please request a new OTP."
Applies to: Email verification, Troubleshooting

Each verification code allows 5 attempts. After the fifth wrong entry the code is dead and no further attempts
against it will be accepted, even correct ones.

Resolution: press Resend code. The attempt counter resets with the new code. There is no lockout on the account
itself and no cooling-off period beyond the usual 60-second resend delay — the user can immediately request a
fresh code and try again.

There is no limit on how many codes a user may request in total.

The usual reason for burning through five attempts is trying the code from an older email (KB-064).

Related: KB-009, KB-010, KB-064

## KB-066 — You keep getting signed out
Applies to: Sessions, Troubleshooting

A normal FOMO session renews itself silently and lasts up to 7 days of continuous use, so a user being signed out
repeatedly — especially within minutes — has an environment problem, not an account problem.

Work through these

1. Cookies are being blocked or cleared. FOMO keeps your session in browser cookies with no fallback. Private/incognito windows, "clear cookies on close" settings, aggressive privacy extensions and strict tracking-protection modes will all sign the user out. This is the cause in the large majority of cases. Ask them to try an ordinary window with extensions disabled.
2. They genuinely have not used FOMO for 7 days. The long-lived pass expires. Signing in again is the fix and it is expected behaviour.
3. They are signed out mid-action, immediately. That pattern points at the account being blocked or deleted rather than a session expiring — check for the specific message (KB-063).
4. Browser clock badly wrong. A device clock off by hours can make a valid session look expired.

There is no "stay signed in" option to enable, no session-timeout setting to lengthen, and no way for a user to see
or manage their active sessions.

Related: KB-014, KB-015, KB-063

## KB-067 — "Too many requests" when signing in
Applies to: Sign-in, Troubleshooting

Sign-in and registration are rate limited to protect against password guessing: roughly 20 attempts per minute
from a single network address, with a small burst allowance. Exceeding it returns an HTTP 429 error.

Resolution: wait a minute and try again. Nothing is locked and no account is penalised — the limit is on the
network address, not the user.

The case worth recognising: the limit counts the whole network, not the individual. A user on a corporate
network, a university campus, a shared office or a mobile carrier's shared address can be blocked by other
people's sign-in attempts, without having done anything themselves. If a user reports being rate limited on their
very first attempt, this is why. Ask them to try from a different network — a mobile hotspot is a quick test.

Only sign-in and registration are limited. Nothing else on the platform is rate limited at all: posting, commenting,
following, messaging and requesting verification codes have no caps.

Related: KB-011, KB-007

## KB-068 — An upload is rejected as too large or the wrong type
Applies to: Media, Troubleshooting

The limits differ depending on what is being uploaded, which is the root of most confusion:

| Uploading | Maximum | Accepted formats |
|---|---|---|
| Profile photo | 5 MB | JPEG, PNG, WebP, GIF |
| Cover photo | 8 MB | JPEG, PNG, WebP, GIF |
| Photo on a post | 5 MB | JPEG, PNG, WebP, GIF |
| Video on a post | 25 MB | MP4 only |
| Chat attachment | 25 MB | The above, plus PDF, DOC, DOCX, TXT |

The three format problems that come up most

1. Video that is not MP4. MOV files from an iPhone, and AVI or WebM files, are all rejected. The user must convert to MP4.
2. Documents on a post. PDFs and Word files can only be sent in chat, never attached to a post.
3. HEIC photos. Modern iPhone photos in HEIC format are not on the accepted list. The user should change their camera setting to "Most Compatible" or export as JPEG.

On size: FOMO does not resize or compress anything, so a 12-megapixel photo really is too big and must be
shrunk before uploading. Any image editor or phone "resize when sharing" option will do it.

The messages are explicit: "File too large. Maximum size is 25 MB" and "Invalid file type. Allowed types: …".
For profile and cover photos the interface catches it first with "Avatar must be under 5MB" or "Cover photo must
be under 8MB".

Related: KB-021, KB-025, KB-047, KB-069

## KB-069 — A very large upload fails with no error message
Applies to: Media, Troubleshooting

If a user uploads something larger than about 30 MB, the request is rejected before it ever reaches FOMO's own
checks. The result is a bare technical error, or an upload that appears to hang and then simply fails — with none of
the friendly "File too large" wording.

This is a recognisable signature: a helpful message means the file was between the app's limit and 30 MB; no
message at all means it was over 30 MB.

Resolution: the file is far too large regardless. Point the user at the real limits in KB-068 — 25 MB is the highest
anything on the platform accepts, so a file this size needs compressing or a shorter video either way.

Related symptom: on a slow connection a large upload can also time out after about two minutes without a clear
message. Smaller files avoid both problems.

Related: KB-068, KB-047, KB-025

## KB-070 — The post published but the photo did not attach
Applies to: Posts, Media, Troubleshooting

The message "Post created, but the attachment failed to upload" means exactly what it says: your text was
published, the file was not.

This happens because FOMO creates the post first and attaches the file afterwards. If the second step fails, the
first is not undone.

Resolution. The media on an existing post cannot be added or changed after the fact — editing a post only edits
its text (KB-026). The user must:

1. Delete the post that published without its picture (KB-027)
2. Check the file against the limits in KB-068 — wrong format and excessive size are the usual causes
3. Post it again

Do not tell the user to edit the post and add the image. There is no control to do so, and they will go looking
for one that does not exist.

If it happens repeatedly with a file that is well within the limits, it is a connection problem — a large file on a
weak connection is the typical case.

Related: KB-025, KB-026, KB-027, KB-068

## KB-071 — The chat screen shows "Offline"
Applies to: Messaging, Troubleshooting

First, correct the usual misunderstanding: the Live/Offline pill describes your own connection, not whether the
other person is online (KB-053). It never indicates anything about the other party.

Second, reassure: chat still works while it says Offline. The screen falls back to checking for new messages
every five seconds, so messages send and arrive with a short delay rather than instantly. Nothing is lost and
nothing needs resending.

If it stays Offline

1. Reload the page. This resolves most cases.
2. Check the network. The live connection is the first thing to drop on an unreliable connection, and the last to come back.
3. Corporate or public networks. Many firewalls and proxies block the kind of persistent connection live chat uses, while leaving ordinary browsing alone. A user who is permanently Offline at the office and Live at home has hit exactly this. There is no workaround beyond changing network — a mobile hotspot will confirm the diagnosis quickly.
4. After a platform update. Deployments drop every live connection at once. Reloading restores it.

The connection retries by itself, backing off up to about 15 seconds between attempts, so it usually recovers
unaided.

Related: KB-053, KB-072, KB-006

## KB-072 — Messages are not arriving
Applies to: Messaging, Troubleshooting

Separate the two cases first — messages you are not receiving, and messages the other person says they never got.

If you are not receiving messages

1. Check the connection pill. If it reads Offline, expect a delay of a few seconds rather than instant delivery (KB-071). Messages still arrive.
2. Reload the conversation. This always fetches the current history from the server.
3. Confirm you are looking at the right conversation. There is only ever one thread per person (KB-044), but users with similar names in their list sometimes open the wrong one.

If the other person says they did not get your message

1. Check whether it actually sent. A failed send shows "Failed to send message." and the message is not delivered — it needs sending again.
2. Check the ticks. A single ✓ means sent but not yet read; ✓✓ means read (KB-051). A message showing a tick did reach FOMO.
3. Check whether you deleted it. Deleting your own message removes it from their copy of the conversation too, and it disappears without trace (KB-049).
4. Consider that they may simply not have opened the conversation. There is no notification for new messages beyond the unread badge (KB-057), so someone not watching the Messages tab may not realise anything arrived.

Message history itself is never lost — it is stored permanently and reloading always retrieves it.

Related: KB-046, KB-049, KB-051, KB-053, KB-071

## KB-073 — The unread badge looks wrong
Applies to: Notifications, Messaging, Troubleshooting

The badges refresh about every 20 seconds, plus whenever you move between screens and immediately when
you read something. A badge that is a few seconds behind is normal.

| Symptom | Explanation |
|---|---|
| Badge shows a count but everything looks read | Wait 20 seconds, or move to another screen and back, to force a refresh |
| Badge does not clear after reading a conversation | Opening a conversation clears it immediately. If it persists, reload |
| Badge stuck at the same number on a poor connection | Deliberate: when the refresh fails, the badge keeps its last known value rather than falsely showing zero |
| Badge shows "99+" | The display caps there. The real number is higher |
| Notification arrived late | Notifications are fetched on a schedule, not pushed (KB-058) |
| No badge for a new message you expected | Messages have their own badge on the Messages tab; they never appear in the notifications list (KB-057) |

Reloading the page always produces accurate counts.

Related: KB-052, KB-056, KB-058

## KB-074 — Catalogue of on-screen messages
Applies to: Troubleshooting, Reference

Every message a user may see, with its cause. Use this to identify a problem from a screenshot.

Sign-up and sign-in

| Message | Cause |
|---|---|
| A user with this email or username already exists | The email, or the username derived from the name, is taken (KB-007) |
| Could not send verification email. Please try registering again. | Mail failure — no account was created (KB-060) |
| Invalid email or password | Wrong credentials, or a social-sign-in account with no password (KB-061) |
| Please verify your email before logging in | Account never verified (KB-062) |
| This account is blocked / suspended / deleted | Administrator action (KB-063) |
| Password must be at least 8 characters | Password too short |
| Passwords do not match | Confirmation field differs |
| Google / GitHub OAuth not configured yet | Social sign-in unavailable on this deployment (KB-012) |

Verification

| Message | Cause |
|---|---|
| Invalid OTP. N attempts remaining. | Wrong code (KB-064) |
| OTP has expired. Please request a new one. | Older than 10 minutes (KB-064) |
| Too many failed attempts. Please request a new OTP. | 5 wrong tries (KB-065) |
| No OTP found. Please request a new one. | No active code (KB-064) |
| Please enter the complete 6-digit code | Fewer than 6 digits entered |

Posts, comments and profile

| Message | Cause |
|---|---|
| Post not found | Deleted, or archived and you are not the author (KB-028) |
| You do not have permission to modify this post | Not your post (KB-026) |
| Archived posts can't be shared | Unarchive it first (KB-028) |
| Original post unavailable | The shared original was deleted or archived (KB-030) |
| Only the comment author or the post owner can delete this comment | Neither applies to you (KB-032) |
| That username is already taken | Choose another (KB-020) |
| Username cannot be empty | Username is required (KB-020) |
| Post created, but the attachment failed to upload | Text published, file not (KB-070) |
| File too large. Maximum size is N MB / Avatar must be under 5MB | Over the limit (KB-068) |
| Invalid file type. Allowed types: … | Unsupported format (KB-068) |

Connections

| Message | Cause |
|---|---|
| You cannot follow yourself | Self-follow attempted |
| You are already following this user | Already followed |
| A pending friend request already exists between you two | One is outstanding in one direction or the other (KB-038) |
| You are already friends with this user | Already friends |
| This friend request has already been resolved | Actioned elsewhere — reload (KB-041) |
| Only the recipient can respond to this friend request | You sent it; you can only cancel (KB-041) |
| Already resolved | Shown in place of Accept/Reject when the request was handled in another tab (KB-039) |

Messaging

| Message | Cause |
|---|---|
| You cannot start a conversation with yourself | Self-message attempted |
| You are not a participant in this conversation | Not your conversation |
| Message must have content or an attachment | Nothing to send (KB-046) |
| You can only modify your own messages | Edit and delete are sender-only (KB-048, KB-049) |
| Failed to upload attachment. | Upload failed — check size and format (KB-047) |

Generic loading failures

Messages of the form "Failed to load feed", "Failed to load conversations.", "Failed to load notifications.", and
similar all indicate a temporary connection or server problem rather than anything specific to the user. Press Try
again or reload. If they persist across networks and devices, the platform itself is having trouble and the case
should be escalated.

Related: KB-060, KB-061, KB-063, KB-068

## KB-075 — Who can use the admin console
Applies to: Administration

Every FOMO account has a role: user or admin. Only admin accounts can reach the admin console.

An Admin tab appears in the navigation bar for administrators only. Ordinary users do not see it.

Someone without the admin role who navigates to an admin address is silently redirected back to their feed.
They get no error and no indication that the area exists.

The console has four sections: Users, Posts, Audit Logs and Stats.

Roles can only be granted by an existing administrator, from the Users screen (KB-076). There is no other
way to make someone an admin — no setting, no self-service, no request flow. If every administrator loses access,
the platform cannot be administered from inside the application at all.

Related: KB-076, KB-082

## KB-076 — The Users screen
Applies to: Administration

Admin → Users lists every account with its username, role, status and join date.

Filters: by status (active, blocked, suspended, deleted) and by role (user, admin). Results are paginated with
Previous and Next.

Row actions

- Edit — opens a dialog to change the account's username (minimum 3 characters) and its role (user or admin). This is the only way to promote someone to administrator.
- Block / Unblock — see KB-077
- Delete — see KB-078

Every action here is confirmed with a dialog stating its effect, and every one is recorded in the audit log
(KB-080).

An administrator cannot see or change a user's password, read their private messages, or change their email
address. Those capabilities do not exist in the console.

Related: KB-075, KB-077, KB-078, KB-080

## KB-077 — Blocking and unblocking a user
Applies to: Administration, Moderation

Block withdraws a user's access to the platform. The confirmation reads: "<user> will lose access to the platform
until unblocked."

What blocking does, immediately

- The account can no longer sign in — it gets "This account is blocked"
- Every existing session ends at once, on every device. A blocked user who is mid-session finds their next action fails; they are not left signed in until their session expires
- Their existing posts, comments and messages remain visible to everyone else. Blocking removes the person, not their content — remove content separately if needed (KB-079)

What blocking does not do

The user is not told, and no email is sent. They see only the sign-in message, with no reason and no appeal
route (KB-057)

Unblocking restores access with the confirmation "<user> will regain access to the platform." Note that the
user must sign in again — their sessions were ended by the block and are not restored.

Blocking is the platform's only tool against harassment, since users cannot block each other (KB-005). It is
therefore the correct response to a harassment report.

Related: KB-018, KB-063, KB-078, KB-082

## KB-078 — Deleting a user account
Applies to: Administration, Moderation

Delete on the Users screen removes an account. The confirmation is explicit: "This is a soft delete — the account
can still be reviewed later. The user will immediately lose access."

What it does

- The account's status becomes deleted and a deletion timestamp is recorded
- All sessions end immediately; the user cannot sign in again
- The account disappears from people search and from public listings
- Their content is not removed. Posts, comments and messages stay where they are

What it is not

It is not an erasure. The record persists and remains visible to administrators, and can be found by filtering the
Users screen by the deleted status. Anyone asking for their data to be genuinely destroyed cannot be satisfied by
this tool.

Users cannot delete their own accounts. There is no account-deletion or deactivation option anywhere in the
interface, so every such request arrives as a support ticket and must be actioned here (KB-082).

Whether a deletion can be reversed is not exposed as a console action — the status filter shows the account, but
there is no "restore" button. Treat deletion as final in practice, and prefer block where the intent is temporary.

Related: KB-018, KB-077, KB-082

## KB-079 — Moderating posts
Applies to: Administration, Moderation

Admin → Posts lists every post on the platform, including archived and deleted ones.

Filters: by author and by status (active, archived, deleted), with pagination.

Actions

- Edit — change the text of any post, inline. The author is not told, and there is no visible marker that a post was edited
- Delete — remove any post. The confirmation reads "Delete this post? This cannot be undone from here."

What deletion does: the post vanishes from feeds, from the author's profile and from search, and the author's
post count drops. Administrators can still see it by filtering for deleted posts. The author is not notified and is
given no reason (KB-057).

There is no reporting or flagging feature anywhere on FOMO — users cannot report a post, and there is no
moderation queue. Every moderation action starts from a support ticket or an administrator noticing something.
There is likewise no automated content filtering of any kind.

Related: KB-077, KB-080, KB-057

## KB-080 — The audit log
Applies to: Administration

Admin → Audit Logs records every administrative action taken on the platform.

Each entry captures the timestamp, which administrator acted, what they did, which account or post it affected,
and the originating IP address.

Actions recorded: user blocked, user unblocked, user deleted, user edited, post edited, post deleted.

Filters: by action, by entity type (user or post), by administrator, and by the specific account or post affected.
There is also a client-side search across the current page.

Pressing View opens a detail dialog with a before and after comparison, field by field — so you can see exactly
what a username was changed from and to, or what a post said before it was edited.

Only administrators can view the audit log.

Two practical uses: confirming what happened to an account when a user disputes it, and confirming that a
requested change was actually carried out.

Related: KB-076, KB-077, KB-079

## KB-081 — The stats dashboard
Applies to: Administration

Admin → Stats gives a platform overview over a selectable window of 7, 30 or 90 days.

Totals: total users, total posts, active posts, archived posts.

Trends over the window: daily signups, daily likes and daily comments, each as a chart.

These are platform-wide figures only. There are no per-user analytics, no engagement metrics for an individual
account, and nothing a user can see about their own reach — a common request that the platform simply does not
serve.

Related: KB-075

## KB-082 — Requests only an administrator can fulfil
Applies to: Administration, Escalation

Several ordinary requests have no self-service path on FOMO and must be escalated. This list is the practical
reason support agents need Part H.

| Request | Why it must be escalated | What the administrator does |
|---|---|---|
| Forgotten password | No password reset exists anywhere (KB-017) | There is no password tool in the console either — confirm identity, and if the account cannot be recovered, the realistic remedy is a new account and deleting the old one (KB-078) |
| Delete my account | No self-service deletion (KB-078) | Delete the account from Admin → Users |
| I'm being harassed | Users cannot block, mute or report (KB-005, KB-045) | Block the offending account (KB-077), and delete the offending posts (KB-079) |
| Remove this post about me | Users can only delete their own posts | Delete the post from Admin → Posts (KB-079) |
| Unblock my account | Only an administrator can reverse a block | Unblock from Admin → Users (KB-077) |
| Make me an administrator | No self-service role change | Edit the user's role from Admin → Users (KB-076) |
| Remove my profile photo | The remove control does not work (KB-022) | Advise replacing the photo; escalate if genuine removal is required |
| Change my email address | Not supported anywhere, for anyone | Cannot be done. The user needs a new account |

Important limits on what an administrator can actually do. The console cannot set or reset passwords, cannot
change email addresses, cannot read private messages, and cannot restore a deleted post or account. Do not
promise a user any of these.

Every administrative action is logged with the acting administrator's identity and IP address (KB-080).

Related: KB-017, KB-022, KB-077, KB-078, KB-079

## KB-083 — Glossary
Applies to: Reference

Terms as FOMO uses them. Several differ from how other platforms use the same word.

- Archive — Hiding one of your own posts from everyone except yourself, reversibly. Not the same as deleting (KB-028).
- Attachment — A file sent in a private message. Chat accepts documents as well as images and video; posts do not (KB-047).
- Avatar — Your profile photo. If you have not set one, FOMO generates an image from your initials (KB-021).
- Block — On FOMO this means an administrator withdrawing an account's access. It does not mean one user blocking another; that feature does not exist (KB-005, KB-077).
- Cover photo — The banner image across the top of your profile (KB-021).
- Display name — The friendly name shown in large type. Separate from your username, need not be unique, and is not what people search for (KB-003).
- Featured creators — The accounts with the most followers. Not personalised; identical for everyone (KB-043).
- Feed — The main screen, with two tabs: For You (everything) and Following (only people you follow). Neither is ranked; both are strictly newest-first (KB-036).
- Follow — A one-way, instant subscription to someone's posts, needing no approval (KB-034).
- Friend — A mutual relationship requiring a request and an acceptance. Accepting also makes both people follow each other (KB-038, KB-039).
- Handle — Another word for username, written @name.
- Live / Offline — The pill on the chat screen showing your own connection status. It says nothing about whether the other person is online (KB-053).
- OTP — "One-time password", the 6-digit code emailed at sign-up. Also called the verification code (KB-009).
- Read receipt — The tick marks on your own messages: one for sent, two for read (KB-051).
- Reply — A comment attached to another comment. Threading goes one level deep only (KB-032).
- Share / repost — Publishing a new post of your own that quotes someone else's. The original author is not notified (KB-030).
- Soft delete — Deletion that hides something from users while keeping the record for administrators. Both post and account deletion work this way (KB-078).
- Suspended — An account status that behaves identically to blocked (KB-018).
- Trending topics — Hashtags drawn from recent posts. A rolling snapshot, not an all-time ranking (KB-043).
- Username — Your unique handle, 3–100 characters. This is the only thing people search matches against (KB-003).

Related: KB-003, KB-004, KB-084

## KB-084 — Every limit and quota in one table
Applies to: Reference

Text length

| Field | Limit |
|---|---|
| Post | 10,000 characters |
| Share caption | 10,000 characters |
| Private message | 5,000 characters |
| Comment or reply | 2,000 characters |
| Bio | 500 characters |
| Display name | 150 characters |
| Username | 3–100 characters |
| Password | 8 characters minimum |
| Emoji reaction | 16 characters |

Posts, comments and messages each need at least one character — except a message carrying an attachment,
which may have no text (KB-046).

File uploads

| Upload | Maximum | Accepted formats |
|---|---|---|
| Profile photo | 5 MB | JPEG, PNG, WebP, GIF |
| Cover photo | 8 MB | JPEG, PNG, WebP, GIF |
| Photo on a post | 5 MB | JPEG, PNG, WebP, GIF |
| Video on a post | 25 MB | MP4 only |
| Chat attachment | 25 MB | The above, plus PDF, DOC, DOCX, TXT |

Anything over roughly 30 MB is rejected before FOMO can show a friendly message (KB-069). One file per
post; no galleries.

Time limits

- Verification code valid for 10 minutes (the screen says 15 — KB-064)
- Verification code attempts 5, then the code is dead
- Resend cooldown 60 seconds
- Session renews every 15 minutes, silently
- Signed in for up to 7 days of continuous use
- Notification and badge refresh About every 20 seconds
- Chat fallback polling when Offline Every 5 seconds

Page sizes

| List | Loaded at a time |
|---|---|
| Feed posts | 20 |
| Followers / following / friends | 20 |
| Conversations | 20 |
| Messages in a conversation | 50 |
| Notifications | 30 |
| Trending topics | 5 |
| Featured creators | 8 |

Comments are the exception: the whole thread loads at once, with no pagination (KB-032).

Rate limits

Sign-in and registration are limited to about 20 attempts per minute per network address (KB-067). Nothing
else on the platform is rate limited — there is no cap on posting, commenting, liking, following, friend requests,
messaging, or requesting verification codes.

Counts that are capped in display only

Unread badges show at most "99+". Like, comment and share counts abbreviate above a thousand (1,800 shows
as "1.8K").

Related: KB-024, KB-068, KB-009, KB-067