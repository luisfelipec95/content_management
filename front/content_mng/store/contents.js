import Fuse from 'fuse.js'

const options = {
    distance: 0,
    keys: [
        "name",
        "description"
    ]
};


export const state = () => ({
    contents: [],
    contentsSearch: [],
    fuse: null,
    currentCategory: '',
})
  
export const getters = {
    getContents(state) {
        return state.contentsSearch;
    },
    getCategory(state) {
        return state.currentCategory;
    }
}

export const mutations = {
    updateContents(state, contents) {
        state.contents = contents;
        state.contentsSearch = state.contents;
    },
    updateCategory(state, category) {
        console.log(category);
        state.currentCategory = category;
    },
    updateFuseEngine(state, contents) {
        state.fuse = new Fuse(contents, options)
    },
    filterContents(state, pattern) {
        if(!pattern)
            state.contentsSearch = state.contents;
        else {
            let result = state.fuse.search(pattern);
            state.contentsSearch = result.map(r => r.item );
            console.log( state.contentsSearch);
        }
        
        //console.log(state.fuse.search(pattern));
    }
}

export const actions = {
    async fetchContents(context) {
        let contents = await this.$axios.$get('/categories/')
        context.commit('updateContents', contents)
        context.commit('updateFuseEngine', contents)
        context.commit('updateCategory', contents[0].name)
    }
}