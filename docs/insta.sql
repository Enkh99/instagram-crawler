
CREATE SEQUENCE public.users_user_id_seq;

CREATE TABLE public.users (
                user_id BIGINT NOT NULL DEFAULT nextval('public.users_user_id_seq'),
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                link TEXT NOT NULL,
                created_date TIMESTAMP NOT NULL,
                is_active BOOLEAN NOT NULL,
                is_deleted BOOLEAN NOT NULL,
                CONSTRAINT users_pk PRIMARY KEY (user_id)
);


ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;

CREATE SEQUENCE public.post_id_seq;

CREATE TABLE public.post (
                id BIGINT NOT NULL DEFAULT nextval('public.post_id_seq'),
                user_id BIGINT NOT NULL,
                post_description TEXT NOT NULL,
                post_date TIMESTAMP NOT NULL,
                post_image_url TEXT NOT NULL,
                post_like BIGINT NOT NULL,
                post_comment TEXT NOT NULL,
                CONSTRAINT post_pk PRIMARY KEY (id)
);


ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;

CREATE SEQUENCE public.scraped_data_id_seq;

CREATE TABLE public.scraped_data (
                id BIGINT NOT NULL DEFAULT nextval('public.scraped_data_id_seq'),
                user_id BIGINT NOT NULL,
                created_at TIMESTAMP NOT NULL,
                name TEXT NOT NULL,
                link_id TEXT NOT NULL,
                followers INTEGER NOT NULL,
                following INTEGER NOT NULL,
                post_number INTEGER NOT NULL,
                total_comment INTEGER NOT NULL,
                total_likes INTEGER NOT NULL,
                CONSTRAINT scraped_data_pk PRIMARY KEY (id)
);


ALTER SEQUENCE public.scraped_data_id_seq OWNED BY public.scraped_data.id;

CREATE SEQUENCE public.followings_id_seq;

CREATE TABLE public.followings (
                id BIGINT NOT NULL DEFAULT nextval('public.followings_id_seq'),
                user_id BIGINT NOT NULL,
                following_account TEXT NOT NULL,
                CONSTRAINT followings_pk PRIMARY KEY (id)
);


ALTER SEQUENCE public.followings_id_seq OWNED BY public.followings.id;

CREATE SEQUENCE public.followers_id_seq;

CREATE TABLE public.followers (
                id BIGINT NOT NULL DEFAULT nextval('public.followers_id_seq'),
                user_id BIGINT NOT NULL,
                follower_account TEXT NOT NULL,
                CONSTRAINT followers_pk PRIMARY KEY (id)
);


ALTER SEQUENCE public.followers_id_seq OWNED BY public.followers.id;

ALTER TABLE public.followers ADD CONSTRAINT user_followers_fk
FOREIGN KEY (user_id)
REFERENCES public.users (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.followings ADD CONSTRAINT user_followings_fk
FOREIGN KEY (user_id)
REFERENCES public.users (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.scraped_data ADD CONSTRAINT user_scraped_data_fk
FOREIGN KEY (user_id)
REFERENCES public.users (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.post ADD CONSTRAINT user_post_fk
FOREIGN KEY (user_id)
REFERENCES public.users (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;