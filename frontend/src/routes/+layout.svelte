<script lang="ts">
  import '../app.css';
  import {
    BarChart3,
    Bell,
    Bot,
    ChevronLeft,
    ChevronRight,
    HelpCircle,
    LayoutDashboard,
    LogOut,
    Moon,
    Newspaper,
    Play,
    Search,
    Settings,
    Shield,
    Sun,
    User,
    Users,
    Building2,
    FileText
  } from 'lucide-svelte';
  import { locale } from '$lib/stores/i18n';
  import { theme } from '$lib/stores/theme';

  let collapsed = false;
  $: currentTheme = $theme;

  const navigation = [
    { name: 'Dashboard', href: '/', icon: LayoutDashboard },
    { name: 'Exercises', href: '/exercises/1', icon: Play, badge: '3' },
    { name: 'Scenarios', href: '/scenarios', icon: FileText },
    { name: 'Crisis Cells', href: '/admin/users', icon: Building2 },
    { name: 'Players', href: '/admin/users', icon: Users },
    { name: 'AI Agents', href: '/admin/ai-agents', icon: Bot },
    { name: 'Media Simulation', href: '/gm/1', icon: Newspaper },
    { name: 'Reports', href: '/', icon: BarChart3 },
    { name: 'Settings', href: '/', icon: Settings }
  ];

  function toggleTheme() {
    theme.set(currentTheme === 'dark' ? 'light' : 'dark');
  }
</script>

<div class="min-h-screen bg-surface-950 text-slate-100 light:bg-surface-50 light:text-slate-950">
  <div class="cyber-grid pointer-events-none fixed inset-0 opacity-80 light:opacity-0"></div>
  <div class="pointer-events-none fixed inset-0 bg-[radial-gradient(ellipse_at_top,rgba(59,130,246,0.12),transparent_55%)] light:hidden"></div>

  <aside
    class={`fixed left-0 top-0 z-40 hidden h-screen flex-col border-r border-slate-800 bg-surface-950/95 backdrop-blur lg:flex light:border-slate-200 light:bg-white ${collapsed ? 'w-16' : 'w-64'}`}
  >
    <div class="flex h-16 items-center gap-3 border-b border-slate-800 px-4 light:border-slate-200">
      <div class="grid h-9 w-9 shrink-0 place-items-center rounded-lg border border-accent-500/25 bg-accent-500/10">
        <Shield size={20} class="text-accent-400" />
      </div>
      {#if !collapsed}
        <div class="min-w-0">
          <div class="truncate text-sm font-semibold">CrisisCommand</div>
          <div class="text-[10px] uppercase text-slate-500">Platform</div>
        </div>
      {/if}
    </div>

    <nav class="flex-1 space-y-1 overflow-y-auto px-2 py-4 text-sm">
      {#each navigation as item}
        <a
          href={item.href}
          class="group relative flex h-10 items-center gap-3 rounded-md px-3 font-medium text-slate-400 transition-colors hover:bg-slate-800/70 hover:text-slate-100 light:text-slate-600 light:hover:bg-slate-100 light:hover:text-slate-950"
        >
          <svelte:component this={item.icon} size={20} class="shrink-0 text-slate-500 group-hover:text-accent-400" />
          {#if !collapsed}
            <span class="truncate">{item.name}</span>
            {#if item.badge}
              <span class="ml-auto rounded-md bg-accent-500/20 px-1.5 py-0.5 text-[10px] text-accent-400">{item.badge}</span>
            {/if}
          {:else if item.badge}
            <span class="absolute right-1 top-1 grid h-4 w-4 place-items-center rounded-full bg-accent-500 text-[10px] text-white">{item.badge}</span>
          {/if}
        </a>
      {/each}
    </nav>

    <div class="border-t border-slate-800 p-2 light:border-slate-200">
      <button
        class="focus-ring grid h-9 w-full place-items-center rounded-md text-slate-400 hover:bg-slate-800 hover:text-slate-100 light:hover:bg-slate-100 light:hover:text-slate-950"
        on:click={() => (collapsed = !collapsed)}
        aria-label="Toggle sidebar"
      >
        {#if collapsed}<ChevronRight size={16} />{:else}<ChevronLeft size={16} />{/if}
      </button>
    </div>
  </aside>

  <div class={`relative z-10 min-h-screen transition-all duration-300 ${collapsed ? 'lg:ml-16' : 'lg:ml-64'}`}>
    <header class="sticky top-0 z-30 flex min-h-16 items-center justify-between gap-4 border-b border-slate-800 bg-surface-900/80 px-4 backdrop-blur light:border-slate-200 light:bg-white/90 lg:px-6">
      <div class="relative hidden w-full max-w-md sm:block">
        <Search class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" size={16} />
        <input
          class="focus-ring h-9 w-full rounded-md border border-slate-800 bg-surface-950/70 pl-9 pr-3 text-sm text-slate-100 placeholder:text-slate-500 light:border-slate-300 light:bg-white light:text-slate-950"
          placeholder="Search exercises, scenarios, players..."
        />
      </div>

      <div class="ml-auto flex items-center gap-2">
        <div class="hidden items-center gap-2 rounded-md border border-signal-green/20 bg-signal-green/10 px-3 py-1.5 text-xs font-medium text-signal-green md:flex">
          <span class="status-dot animate-pulse bg-signal-green"></span>
          3 Live Exercises
        </div>
        <select bind:value={$locale} class="h-9 rounded-md border border-slate-800 bg-surface-950 px-2 text-sm light:border-slate-300 light:bg-white">
          <option value="fr">FR</option>
          <option value="en">EN</option>
        </select>
        <button class="focus-ring grid h-9 w-9 place-items-center rounded-md border border-slate-800 text-slate-400 hover:text-slate-100 light:border-slate-300 light:hover:text-slate-950" on:click={toggleTheme} aria-label="Theme">
          {#if currentTheme === 'dark'}<Sun size={16} />{:else}<Moon size={16} />{/if}
        </button>
        <button class="focus-ring relative grid h-9 w-9 place-items-center rounded-md text-slate-400 hover:bg-slate-800 hover:text-slate-100 light:hover:bg-slate-100 light:hover:text-slate-950" aria-label="Notifications">
          <Bell size={19} />
          <span class="absolute right-1 top-1 grid h-4 w-4 place-items-center rounded-full bg-signal-red text-[10px] text-white">5</span>
        </button>
        <button class="focus-ring hidden h-9 w-9 place-items-center rounded-md text-slate-400 hover:bg-slate-800 hover:text-slate-100 light:hover:bg-slate-100 light:hover:text-slate-950 sm:grid" aria-label="Help">
          <HelpCircle size={19} />
        </button>
        <div class="hidden items-center gap-2 rounded-md px-2 py-1 sm:flex">
          <div class="grid h-8 w-8 place-items-center rounded-full bg-accent-500/20 text-accent-400">
            <User size={16} />
          </div>
          <div class="leading-tight">
            <div class="text-sm font-medium">Sarah Chen</div>
            <div class="text-[10px] text-slate-500">Game Master</div>
          </div>
        </div>
        <a class="focus-ring grid h-9 w-9 place-items-center rounded-md text-slate-400 hover:bg-slate-800 hover:text-slate-100 light:hover:bg-slate-100 light:hover:text-slate-950" href="/auth/login" aria-label="Sign out">
          <LogOut size={18} />
        </a>
      </div>
    </header>

    <main class="p-4 lg:p-6">
      <slot />
    </main>
  </div>
</div>
