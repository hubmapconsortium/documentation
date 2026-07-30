const initSankey = async () => {
    const sankeyOptions = btoa(
        JSON.stringify({
            startUpOnOptions: false,
            disableUbkgColorPalettes: true,
            useShadow: true,
            isProd: true,
            styleSheetPath: '/data-sankey/xac-sankey.css',
            groupByOrganCategoryKey: 'term',
            api: {
                sankey: 'https://entity.api.hubmapconsortium.org/datasets/sankey_data',
                context: 'hubmap'
            }
        })
    );
    const el = document.getElementById('js-sankey')
    el.innerHTML = `<consortia-sankey options="${sankeyOptions}" />`

    const i = setInterval(() => {
        const ctx = document.querySelector('consortia-sankey')
        if (ctx.setOptions) {
            let adapter = new HuBMAPAdapter(ctx, {isProd: true})
            clearInterval(i)
            // clear color settings & leave HM to be its current randomized color (matching the data ingest board) until otherwise requested
            ctx.theme.byScheme = undefined
            ctx.setOptions(
                {
                    
                    startUpOnOptions: true,
                    onDataBuildCallback: () => {
                        adapter.onDataBuildCallback()
                    },
                    onLinkClickCallback: (e, d) => {
                        e.preventDefault()
                        adapter.goToFromLink(d)
                    },
                    onNodeClickCallback: (e, d) => {
                        e.preventDefault()
                        adapter.goToFromNode(d)
                    },
                    onLabelClickCallback: (e, d) => {
                        e.preventDefault()
                        adapter.goToFromNode(d)
                    },
                }
            )
        }
    }, 500)
}

initSankey()