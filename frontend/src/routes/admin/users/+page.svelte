<script lang="ts">
  import Button from '$lib/components/Button.svelte';
  import DataTable from '$lib/components/DataTable.svelte';
  import Panel from '$lib/components/Panel.svelte';

  const columns = ['first name', 'last name', 'email', 'role', 'MFA enabled', 'crisis cells', 'status'];
  const rows = [
    { 'first name': 'Lea', 'last name': 'Martin', email: 'lea@example.com', role: 'Game Master', 'MFA enabled': true, 'crisis cells': 'Comms', status: 'Active' },
    { 'first name': 'Nadir', 'last name': 'Khan', email: 'nadir@example.com', role: 'Observer', 'MFA enabled': false, 'crisis cells': 'Legal', status: 'Invited' }
  ];
</script>

<div class="grid gap-4 p-4 xl:grid-cols-[1fr_360px]">
  <section>
    <div class="mb-3 flex items-center justify-between">
      <input class="h-9 w-80 rounded-md border border-slate-700 bg-surface-900 px-3 text-sm light:border-slate-300 light:bg-white" placeholder="Search users" />
      <Button>Invite user</Button>
    </div>
    <DataTable {columns} {rows} />
  </section>
  <Panel title="Profile">
    <div class="space-y-4 text-sm">
      <div>
        <div class="font-medium">Effective rights</div>
        <div class="text-slate-400">exercise.launch, channel.observe, audit.read</div>
      </div>
      <div>
        <div class="font-medium">Exercise history</div>
        <div class="text-slate-400">3 completed, 1 running</div>
      </div>
      <div>
        <div class="font-medium">Audit activity</div>
        <div class="text-slate-400">Last login 12 minutes ago</div>
      </div>
    </div>
  </Panel>
</div>
