<script lang="ts">
  import Panel from '$lib/components/Panel.svelte';
</script>

<div class="grid h-[calc(100vh-3.5rem)] grid-cols-[240px_1fr_320px] overflow-hidden">
  <aside class="border-r border-slate-800 bg-surface-900 p-3 text-sm light:border-slate-200 light:bg-white">
    <div class="mb-3 font-semibold">Channels</div>
    {#each ['general', 'executive-cell', 'legal-private', 'soc-ops'] as channel}
      <div class="rounded-md px-2 py-1.5 hover:bg-slate-800 light:hover:bg-slate-100"># {channel}</div>
    {/each}
    <div class="mt-6 mb-3 font-semibold">Direct messages</div>
    {#each ['AI Journalist', 'Game Master', 'Legal lead'] as dm}
      <div class="rounded-md px-2 py-1.5 hover:bg-slate-800 light:hover:bg-slate-100">{dm}</div>
    {/each}
  </aside>

  <section class="flex min-w-0 flex-col">
    <header class="flex h-12 items-center justify-between border-b border-slate-800 px-4 text-sm light:border-slate-200">
      <div class="font-semibold">Ransomware tabletop / general</div>
      <div class="text-slate-400">00:42:18 · Running · 42 active</div>
    </header>
    <div class="flex-1 space-y-4 overflow-auto p-4">
      {#each [
        ['SOC Analyst', 'Role: Player', 'We are seeing encryption activity on two file servers.'],
        ['AI Journalist', 'AI', 'Can you confirm whether customer data has been affected?'],
        ['Game Master', 'GM', 'Stimulus injected: fake news article published.']
      ] as msg}
        <article class="flex gap-3">
          <div class="grid h-9 w-9 shrink-0 place-items-center rounded-md bg-accent-600 text-sm font-semibold">{msg[0][0]}</div>
          <div>
            <div class="flex items-center gap-2 text-sm"><span class="font-medium">{msg[0]}</span><span class="rounded bg-slate-800 px-1.5 py-0.5 text-xs text-slate-300 light:bg-slate-100 light:text-slate-600">{msg[1]}</span></div>
            <p class="mt-1 text-sm text-slate-300 light:text-slate-700">{msg[2]}</p>
          </div>
        </article>
      {/each}
    </div>
    <div class="border-t border-slate-800 p-3 light:border-slate-200">
      <input class="h-10 w-full rounded-md border border-slate-700 bg-surface-900 px-3 text-sm light:border-slate-300 light:bg-white" placeholder="Message #general" />
    </div>
  </section>

  <aside class="space-y-4 overflow-auto border-l border-slate-800 bg-surface-900 p-3 light:border-slate-200 light:bg-white">
    <Panel title="Participants" dense><div class="text-sm text-slate-400">42 active · 8 crisis cells</div></Panel>
    <Panel title="Current objectives" dense><div class="text-sm">Assess impact, coordinate public response, prepare executive brief.</div></Panel>
    <Panel title="Recent stimuli" dense><div class="text-sm text-slate-400">Fake news, EDR alert, customer email</div></Panel>
  </aside>
</div>
