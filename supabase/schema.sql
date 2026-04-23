create extension if not exists "pgcrypto";

create table if not exists public.profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  email text,
  display_name text not null default 'Learner',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.progress_states (
  user_id uuid not null references auth.users(id) on delete cascade,
  page_id text not null,
  state_json jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (user_id, page_id)
);

create table if not exists public.workspace_states (
  user_id uuid not null references auth.users(id) on delete cascade,
  workspace_key text not null default 'global',
  state_json jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (user_id, workspace_key)
);

create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists set_profiles_updated_at on public.profiles;
create trigger set_profiles_updated_at
before update on public.profiles
for each row execute procedure public.set_updated_at();

drop trigger if exists set_progress_states_updated_at on public.progress_states;
create trigger set_progress_states_updated_at
before update on public.progress_states
for each row execute procedure public.set_updated_at();

drop trigger if exists set_workspace_states_updated_at on public.workspace_states;
create trigger set_workspace_states_updated_at
before update on public.workspace_states
for each row execute procedure public.set_updated_at();

alter table public.profiles enable row level security;
alter table public.progress_states enable row level security;
alter table public.workspace_states enable row level security;

drop policy if exists "profiles_select_own" on public.profiles;
create policy "profiles_select_own"
on public.profiles
for select
to authenticated
using ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "profiles_insert_own" on public.profiles;
create policy "profiles_insert_own"
on public.profiles
for insert
to authenticated
with check ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "profiles_update_own" on public.profiles;
create policy "profiles_update_own"
on public.profiles
for update
to authenticated
using ((select auth.uid()) is not null and (select auth.uid()) = user_id)
with check ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "progress_select_own" on public.progress_states;
create policy "progress_select_own"
on public.progress_states
for select
to authenticated
using ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "progress_insert_own" on public.progress_states;
create policy "progress_insert_own"
on public.progress_states
for insert
to authenticated
with check ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "progress_update_own" on public.progress_states;
create policy "progress_update_own"
on public.progress_states
for update
to authenticated
using ((select auth.uid()) is not null and (select auth.uid()) = user_id)
with check ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "workspace_select_own" on public.workspace_states;
create policy "workspace_select_own"
on public.workspace_states
for select
to authenticated
using ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "workspace_insert_own" on public.workspace_states;
create policy "workspace_insert_own"
on public.workspace_states
for insert
to authenticated
with check ((select auth.uid()) is not null and (select auth.uid()) = user_id);

drop policy if exists "workspace_update_own" on public.workspace_states;
create policy "workspace_update_own"
on public.workspace_states
for update
to authenticated
using ((select auth.uid()) is not null and (select auth.uid()) = user_id)
with check ((select auth.uid()) is not null and (select auth.uid()) = user_id);
