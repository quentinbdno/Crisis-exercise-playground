<script lang="ts">
  import '../app.css';
  import { Moon, Sun } from 'lucide-svelte';
  import { locale, t } from '$lib/stores/i18n';
  import { theme, type Theme } from '$lib/stores/theme';

  $: currentTheme = $theme;
  $: currentLocale = $locale;

  function toggleTheme() {
    theme.set(currentTheme === 'dark' ? 'light' : 'dark');
  }
</script>

<div class="min-h-screen bg-surface-950 text-slate-100 light:bg-surface-50 light:text-slate-950">
  <div class="flex min-h-screen">
    <aside class="hidden w-64 border-r border-slate-800 bg-surface-900 px-3 py-4 light:border-slate-200 light:bg-white lg:block">
      <div class="mb-6 px-2 text-sm font-semibold">{t(currentLocale, 'app')}</div>
      <nav class="space-y-1 text-sm">
        <a class="block rounded-md px-3 py-2 hover:bg-slate-800 light:hover:bg-slate-100" href="/">{t(currentLocale, 'dashboard')}</a>
        <a class="block rounded-md px-3 py-2 hover:bg-slate-800 light:hover:bg-slate-100" href="/admin/users">{t(currentLocale, 'users')}</a>
        <a class="block rounded-md px-3 py-2 hover:bg-slate-800 light:hover:bg-slate-100" href="/admin/ai-agents">{t(currentLocale, 'agents')}</a>
        <a class="block rounded-md px-3 py-2 hover:bg-slate-800 light:hover:bg-slate-100" href="/scenarios">{t(currentLocale, 'scenarios')}</a>
        <a class="block rounded-md px-3 py-2 hover:bg-slate-800 light:hover:bg-slate-100" href="/exercises/1">{t(currentLocale, 'exercises')}</a>
        <a class="block rounded-md px-3 py-2 hover:bg-slate-800 light:hover:bg-slate-100" href="/gm/1">{t(currentLocale, 'gameMaster')}</a>
      </nav>
    </aside>

    <main class="min-w-0 flex-1">
      <header class="flex h-14 items-center justify-between border-b border-slate-800 bg-surface-900 px-4 light:border-slate-200 light:bg-white">
        <div class="text-sm text-slate-400 light:text-slate-600">API-first crisis simulation platform</div>
        <div class="flex items-center gap-2">
          <select bind:value={$locale} class="h-9 rounded-md border border-slate-700 bg-surface-950 px-2 text-sm light:border-slate-300 light:bg-white">
            <option value="fr">FR</option>
            <option value="en">EN</option>
          </select>
          <button class="focus-ring grid h-9 w-9 place-items-center rounded-md border border-slate-700 light:border-slate-300" on:click={toggleTheme} aria-label="Theme">
            {#if currentTheme === 'dark'}<Sun size={16} />{:else}<Moon size={16} />{/if}
          </button>
        </div>
      </header>
      <slot />
    </main>
  </div>
</div>
