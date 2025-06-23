const initSankey = async () => {
    const sankeyOptions = btoa(
        JSON.stringify({
            useShadow: true,
            isProd: true,
            styleSheetPath: '/data-sankey/xac-sankey.css',
            validFilterMap: {
                dataset_type: 'dataset_type_hierarchy',
                status: null,
                source_type: 'dataset_source_type',
            },
            groupByOrganCategoryKey: 'term',
            api: {
                sankey: 'https://entity-api.dev.hubmapconsortium.org/datasets/sankey_data',
                context: 'hubmap'
            }
        })
    )
    const el = document.getElementById('js-sankey')
    el.innerHTML = `<consortia-sankey options="${sankeyOptions}" />`

    const i = setInterval(() => {
        const ctx = document.querySelector('consortia-sankey')
        if (ctx.setOptions) {
            let adapter = new HuBMAPAdapter(ctx, {isProd: true})
            clearInterval(i)
            ctx.setOptions({
                onDataBuildCallback: () => adapter.onDataBuildCallback(),
                onNodeBuildCssCallback: (d) => {
                    if (d.columnName === ctx.validFilterMap.dataset_type) {
                        const assay = adapter.captureByKeysValue({matchKey: d.columnName, matchValue: d.name, keepKey: 'dataset_type_description'}, ctx.rawData)
                        return assay.length <= 0 ? 'c-sankey__node--default' : ''
                    }
                    return ''
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
                }
            })
        }
    }, 500)
}

initSankey()