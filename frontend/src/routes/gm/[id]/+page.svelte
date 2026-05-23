<script lang="ts">
  import Button from '$lib/components/Button.svelte';
  import Panel from '$lib/components/Panel.svelte';
</script>

<div class="space-y-4 p-4">
  <div class="flex flex-wrap gap-2">
    <Button>Launch</Button>
    <Button variant="ghost">Pause</Button>
    <Button variant="ghost">Resume</Button>
    <Button variant="ghost">Accelerate timeline</Button>
    <Button variant="ghost">Inject manual stimulus</Button>
    <Button variant="ghost">Resend stimulus</Button>
  </div>

  <div class="grid gap-4 xl:grid-cols-3">
    <Panel title="Global timeline"><div class="text-sm text-slate-400">00:45 Fake news · 00:52 CEO call · 01:05 regulator email</div></Panel>
    <Panel title="Upcoming stimuli"><div class="text-sm text-slate-400">5 scheduled · 1 retry pending</div></Panel>
    <Panel title="Delivery status"><div class="text-sm text-slate-400">124 delivered · 2 failed · 3 pending</div></Panel>
    <Panel title="Active channels"><div class="text-sm text-slate-400">general, legal-private, soc-ops</div></Panel>
    <Panel title="Unanswered questions"><div class="text-sm text-slate-400">AI journalist awaits official statement</div></Panel>
    <Panel title="AI activity"><div class="text-sm text-slate-400">4 agents active · 12 prompts in last hour</div></Panel>
  </div>

  <Panel title="Audit stream">
    <div class="space-y-2 text-sm text-slate-400">
      <div>exercise.launched by Game Master</div>
      <div>stimulus.delivered fake_news #32</div>
      <div>message.created by AI Journalist</div>
    </div>
  </Panel>
</div>
