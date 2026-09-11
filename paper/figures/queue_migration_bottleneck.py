import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from pathlib import Path
out=Path(__file__).with_name('queue_migration_bottleneck.pdf')
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(7.2,3.0),gridspec_kw={'width_ratios':[1.05,1.35]})
labels=['generation','evaluation','integration','maintenance','retirement']
colors=['#d9d9d9','#4c78a8','#f58518','#54a24b','#e45756']
cmap=ListedColormap(colors)
# synthetic generation sweep: 1,2,4 remain generation-bound; 8 moves to evaluation
m1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1]]
# reshape rows as stage x condition; show one cell per workload/seed replicated pattern
im=ax1.imshow(m1,aspect='auto',cmap=cmap,vmin=0,vmax=4)
ax1.set_xticks(range(4),['1','2','4','8']); ax1.set_xlabel('generation rate')
ax1.set_yticks(range(5),labels); ax1.set_title('Generation sweep')
# release ladder diagonal: constrained stage localizes to itself
m2=[[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,4],[0,0,0,0]]
ax2.imshow(m2,aspect='auto',cmap=cmap,vmin=0,vmax=4)
ax2.set_xticks(range(4),['eval.','integr.','maint.','retire.']); ax2.set_xlabel('released capacity except')
ax2.set_yticks(range(5),labels); ax2.set_title('Capacity-release ladder')
for ax in (ax1,ax2):
    ax.tick_params(length=0); ax.spines[['top','right','left','bottom']].set_visible(False)
fig.suptitle('Bottleneck localization in the frozen synthetic v3 protocol',fontsize=10)
fig.tight_layout(rect=[0,0,1,0.93])
fig.savefig(out,bbox_inches='tight')
