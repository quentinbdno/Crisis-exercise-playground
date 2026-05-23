<script lang="ts">
  import Panel from '$lib/components/Panel.svelte';
</script>

<svelte:head><title>Crisis Exercise</title></svelte:head>

<div class="space-y-4 p-4">
  <div class="grid gap-4 xl:grid-cols-4">
    {#each [
      ['Running exercises', '3', '2 with active stimuli'],
      ['Scheduled stimuli', '128', 'Next injection in 04:32'],
      ['Active participants', '42', '8 crisis cells online'],
      ['AI agents', '11', '4 currently assigned']
    ] as card}
      <section class="border-y border-slate-800 bg-surface-900 p-4 light:border-slate-200 light:bg-white">
        <div class="text-xs uppercase text-slate-400">{card[0]}</div>
        <div class="mt-3 text-3xl font-semibold">{card[1]}</div>
        <div class="mt-1 text-sm text-slate-400">{card[2]}</div>
      </section>
    {/each}
  </div>

  <div class="grid gap-4 xl:grid-cols-[1.4fr_1fr]">
    <Panel title="Operational timeline">
      <div class="space-y-3 text-sm">
        {#each ['08:00 - Exercise launched', '08:12 - Fake news stimulus delivered', '08:19 - AI journalist asked follow-up', '08:27 - Legal cell joined private channel'] as item}
          <div class="flex items-center gap-3 border-b border-slate-800 pb-3 light:border-slate-200">
            <span class="h-2 w-2 rounded-full bg-accent-500"></span>
            <span>{item}</span>
          </div>
        {/each}
      </div>
    </Panel>
    <Panel title="Enterprise readiness">
      <div class="grid gap-2 text-sm text-slate-300 light:text-slate-700">
        <div>REST and WebSocket separation</div>
        <div>RBAC and crisis-cell isolation</div>
        <div>Scenario ZIP/YAML/CSV workflows</div>
        <div>Audit-first orchestration</div>
      </div>
    </Panel>
  </div>
</div>
