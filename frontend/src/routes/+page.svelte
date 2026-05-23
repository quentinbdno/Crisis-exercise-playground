<script lang="ts">
  import {
    AlertTriangle,
    ArrowRight,
    ArrowUpRight,
    Bot,
    Building2,
    CheckCircle2,
    Clock,
    MoreHorizontal,
    Pause,
    Play,
    Users,
    Zap
  } from 'lucide-svelte';
  import Button from '$lib/components/Button.svelte';

  const stats = [
    { label: 'Active Exercises', value: '3', detail: '2 new this week', tone: 'primary', icon: Play },
    { label: 'Connected Players', value: '54', detail: '48 active now', tone: 'success', icon: Users },
    { label: 'Open Incidents', value: '12', detail: '3 critical, 5 high', tone: 'warning', icon: AlertTriangle },
    { label: 'AI Agents Online', value: '2', detail: '20 tasks completed today', tone: 'primary', icon: Bot }
  ];

  const activeExercises = [
    { name: 'Operation Blackout', type: 'Ransomware Response', status: 'Live', progress: 65, players: 24, time: '2h 15m', severity: 'critical' },
    { name: 'Storm Shield', type: 'Data Breach Scenario', status: 'Live', progress: 32, players: 18, time: '45m', severity: 'high' },
    { name: 'Phoenix Protocol', type: 'Business Continuity', status: 'Paused', progress: 78, players: 12, time: '4h 30m', severity: 'medium' }
  ];

  const stimuli = [
    { time: '5m', type: 'Fake Tweet', target: 'All Players', description: 'Ransomware group claims responsibility' },
    { time: '12m', type: 'Email', target: 'IT Cell', description: 'Vendor requesting emergency access' },
    { time: '18m', type: 'News Article', target: 'Comms Cell', description: 'Media outlet reports data breach' },
    { time: '25m', type: 'Phone Call', target: 'Executive Cell', description: 'Board member inquiry' }
  ];

  const activity = [
    ['2m ago', 'John Mitchell', 'responded to ransomware alert'],
    ['5m ago', 'AI Agent', 'injected fake journalist message'],
    ['8m ago', 'Sarah Chen', 'paused Phoenix Protocol'],
    ['12m ago', 'Crisis Cell A', 'escalated incident #42']
  ];

  const cells = [
    ['IT Response', '8 members', '3 incidents', true],
    ['Executive Team', '5 members', '1 incident', true],
    ['Communications', '6 members', '2 incidents', true],
    ['Legal & Compliance', '4 members', '0 incidents', false]
  ];

  function iconTone(tone: string) {
    if (tone === 'success') return 'bg-signal-green/10 text-signal-green';
    if (tone === 'warning') return 'bg-signal-amber/10 text-signal-amber';
    return 'bg-accent-500/10 text-accent-400';
  }
</script>

<svelte:head><title>CrisisCommand Dashboard</title></svelte:head>

<div class="space-y-6">
  <section class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
    <div>
      <h1 class="text-2xl font-semibold text-slate-50 light:text-slate-950">Dashboard</h1>
      <p class="mt-1 text-sm text-slate-400 light:text-slate-600">Monitor active exercises and platform activity</p>
    </div>
    <div class="flex flex-wrap items-center gap-3">
      <Button variant="ghost"><Clock size={16} />Exercise History</Button>
      <Button><Play size={16} />New Exercise</Button>
    </div>
  </section>

  <section class="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
    {#each stats as stat}
      <article class="rounded-lg border border-slate-800 bg-surface-900/85 p-4 shadow-panel light:border-slate-200 light:bg-white">
        <div class="flex items-center justify-between gap-3">
          <div>
            <p class="text-sm text-slate-400 light:text-slate-600">{stat.label}</p>
            <p class="mt-1 text-3xl font-semibold">{stat.value}</p>
          </div>
          <div class={`grid h-12 w-12 place-items-center rounded-lg ${iconTone(stat.tone)}`}>
            <svelte:component this={stat.icon} size={24} />
          </div>
        </div>
        <div class="mt-3 flex items-center gap-1 text-xs text-slate-400 light:text-slate-600">
          {#if stat.tone === 'primary'}<ArrowUpRight size={13} class="text-signal-green" />{/if}
          <span>{stat.detail}</span>
        </div>
      </article>
    {/each}
  </section>

  <section class="grid gap-6 xl:grid-cols-[1.45fr_0.85fr]">
    <div class="space-y-4">
      <article class="rounded-lg border border-slate-800 bg-surface-900/85 light:border-slate-200 light:bg-white">
        <header class="flex items-center justify-between gap-4 border-b border-slate-800 px-4 py-3 light:border-slate-200">
          <div>
            <h2 class="text-base font-medium">Active Exercises</h2>
            <p class="text-sm text-slate-400 light:text-slate-600">Currently running crisis simulations</p>
          </div>
          <a class="inline-flex items-center gap-1 text-sm text-slate-400 hover:text-slate-100 light:hover:text-slate-950" href="/exercises/1">
            View all <ArrowRight size={16} />
          </a>
        </header>
        <div class="space-y-3 p-4">
          {#each activeExercises as exercise}
            <div class="rounded-lg border border-slate-800 bg-surface-800/45 p-4 transition-colors hover:border-accent-500/40 light:border-slate-200 light:bg-slate-50">
              <div class="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
                <div class="min-w-0 flex-1">
                  <div class="flex flex-wrap items-center gap-2">
                    <h3 class="font-medium">{exercise.name}</h3>
                    <span class={`inline-flex items-center rounded-md border px-2 py-0.5 text-xs ${exercise.status === 'Live' ? 'border-signal-green/30 bg-signal-green/10 text-signal-green' : 'border-slate-700 bg-slate-800 text-slate-300'}`}>
                      {#if exercise.status === 'Live'}
                        <span class="mr-1.5 h-1.5 w-1.5 rounded-full bg-signal-green"></span>
                      {:else}
                        <Pause size={12} class="mr-1" />
                      {/if}
                      {exercise.status}
                    </span>
                    <span class={`rounded-md border px-2 py-0.5 text-xs ${exercise.severity === 'critical' ? 'border-signal-red/50 text-signal-red' : exercise.severity === 'high' ? 'border-signal-amber/50 text-signal-amber' : 'border-slate-600 text-slate-400'}`}>
                      {exercise.severity}
                    </span>
                  </div>
                  <p class="mt-1 text-sm text-slate-400 light:text-slate-600">{exercise.type}</p>
                  <div class="mt-3 flex flex-wrap items-center gap-4 text-xs text-slate-400 light:text-slate-600">
                    <span class="inline-flex items-center gap-1"><Users size={14} />{exercise.players} players</span>
                    <span class="inline-flex items-center gap-1"><Clock size={14} />{exercise.time} elapsed</span>
                  </div>
                </div>
                <div class="w-full shrink-0 space-y-2 lg:w-36">
                  <a href="/gm/1" class="focus-ring inline-flex h-9 w-full items-center justify-center gap-1 rounded-md bg-accent-600 px-3 text-sm font-medium text-white hover:bg-accent-500">
                    <Zap size={14} />Control Room
                  </a>
                  <div>
                    <div class="mb-1 flex items-center justify-between text-xs">
                      <span class="text-slate-400">Progress</span>
                      <span class="font-medium">{exercise.progress}%</span>
                    </div>
                    <div class="h-1.5 overflow-hidden rounded-full bg-slate-800 light:bg-slate-200">
                      <div class="h-full rounded-full bg-accent-500" style={`width: ${exercise.progress}%`}></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          {/each}
        </div>
      </article>

      <article class="rounded-lg border border-slate-800 bg-surface-900/85 light:border-slate-200 light:bg-white">
        <header class="border-b border-slate-800 px-4 py-3 light:border-slate-200">
          <h2 class="text-base font-medium">Upcoming Stimuli</h2>
          <p class="text-sm text-slate-400 light:text-slate-600">Next automated injects across live exercises</p>
        </header>
        <div class="divide-y divide-slate-800 light:divide-slate-200">
          {#each stimuli as item}
            <div class="grid gap-3 px-4 py-3 text-sm sm:grid-cols-[64px_120px_1fr_auto] sm:items-center">
              <span class="font-mono text-accent-400">T+{item.time}</span>
              <span class="rounded-md bg-slate-800 px-2 py-1 text-xs text-slate-300 light:bg-slate-100 light:text-slate-700">{item.type}</span>
              <div>
                <div class="font-medium">{item.description}</div>
                <div class="text-xs text-slate-400 light:text-slate-600">{item.target}</div>
              </div>
              <button class="focus-ring grid h-8 w-8 place-items-center rounded-md text-slate-400 hover:bg-slate-800 hover:text-slate-100 light:hover:bg-slate-100 light:hover:text-slate-950" aria-label="Stimulus actions">
                <MoreHorizontal size={16} />
              </button>
            </div>
          {/each}
        </div>
      </article>
    </div>

    <aside class="space-y-4">
      <article class="rounded-lg border border-slate-800 bg-surface-900/85 light:border-slate-200 light:bg-white">
        <header class="border-b border-slate-800 px-4 py-3 light:border-slate-200">
          <h2 class="text-base font-medium">Crisis Cells</h2>
          <p class="text-sm text-slate-400 light:text-slate-600">Readiness by response group</p>
        </header>
        <div class="space-y-3 p-4">
          {#each cells as cell}
            <div class="flex items-center justify-between rounded-lg bg-surface-800/50 p-3 light:bg-slate-50">
              <div class="flex items-center gap-3">
                <div class="grid h-9 w-9 place-items-center rounded-lg bg-accent-500/10 text-accent-400">
                  <Building2 size={17} />
                </div>
                <div>
                  <div class="text-sm font-medium">{cell[0]}</div>
                  <div class="text-xs text-slate-400 light:text-slate-600">{cell[1]} · {cell[2]}</div>
                </div>
              </div>
              {#if cell[3]}
                <CheckCircle2 size={17} class="text-signal-green" />
              {:else}
                <span class="rounded-md bg-slate-800 px-2 py-1 text-xs text-slate-400 light:bg-slate-100">Standby</span>
              {/if}
            </div>
          {/each}
        </div>
      </article>

      <article class="rounded-lg border border-slate-800 bg-surface-900/85 light:border-slate-200 light:bg-white">
        <header class="border-b border-slate-800 px-4 py-3 light:border-slate-200">
          <h2 class="text-base font-medium">Activity Feed</h2>
          <p class="text-sm text-slate-400 light:text-slate-600">Latest platform events</p>
        </header>
        <div class="space-y-4 p-4">
          {#each activity as event}
            <div class="flex gap-3">
              <span class="mt-1.5 h-2 w-2 shrink-0 rounded-full bg-accent-500"></span>
              <div>
                <div class="text-sm"><span class="font-medium">{event[1]}</span> {event[2]}</div>
                <div class="text-xs text-slate-500">{event[0]}</div>
              </div>
            </div>
          {/each}
        </div>
      </article>
    </aside>
  </section>
</div>
