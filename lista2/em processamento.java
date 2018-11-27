XdrManageSearchRequest
import static br.com.telecomassociates.xdrcommons.SearchStatusUtil.checkStatusSearchRequest;

SearchStatus value = checkStatusSearchRequest(search.getStatus(),search.getProcessingItems(),
						search.getQueuedItems(),search.getProcessedItems(),
						search.getSearchSqlItems().size() + search.getSearchItems().size());

SearchStatusUtil
package br.com.telecomassociates.xdrcommons;

import br.com.telecomassociates.xdrbeans.beans.SearchStatus;

public class SearchStatusUtil {

    public static SearchStatus checkStatusSearchRequest(SearchStatus status, int processingCount, int queuedCount, int processedCount,
                                 int searchItemsSize){

        if(!status.equals(SearchStatus.NOT_SUBMITTED)) {
            if (processingCount > 0) {
                status = SearchStatus.PROCESSING;
            } else if (queuedCount > 0 && queuedCount + processedCount == searchItemsSize ) {
                status = SearchStatus.QUEUED;
            }
        }
        return status;
    }
}


import static br.com.telecomassociates.xdrcommons.SearchStatusUtil.checkStatusSearchRequest;
int i = 0;
SearchStatus status = checkStatusSearchRequest(search.getStatus(),search.getProcessingItems(),search.getQueuedItems(),search.getProcessedItems(),
						search.getSearchSqlItems().size() + search.getSearchItems().size());

				search.setStatus(status);
				search.setObservation(searchRS.getString(15));
				if(listStatusIndex.contains(status.ordinal())){
					listResult.add(search);
				}

