""" 
__init__.py for the prompts folder
"""

from .generate_answer_node_prompts import TEMPLATE_CHUNKS, TEMPLATE_NO_CHUNKS, TEMPLATE_MERGE, TEMPLATE_CHUNKS_MD, TEMPLATE_NO_CHUNKS_MD, TEMPLATE_MERGE_MD
from .generate_answer_node_csv_prompts import TEMPLATE_CHUKS_CSV, TEMPLATE_NO_CHUKS_CSV, TEMPLATE_MERGE_CSV  
from .generate_answer_node_pdf_prompts import TEMPLATE_CHUNKS_PDF, TEMPLATE_NO_CHUNKS_PDF, TEMPLATE_MERGE_PDF
from .generate_answer_node_omni_prompts import TEMPLATE_CHUNKS_OMNI, TEMPLATE_NO_CHUNKS_OMNI, TEMPLATE_MERGE_OMNI
from .merge_answer_node_prompts import TEMPLATE_COMBINED
from .robots_node_prompts import TEMPLATE_ROBOT
from .search_internet_node_prompts import TEMPLATE_SEARCH_INTERNET
from .search_link_node_prompts import TEMPLATE_RELEVANT_LINKS
from .search_node_with_context_prompts import TEMPLATE_SEARCH_WITH_CONTEXT_CHUNKS, TEMPLATE_SEARCH_WITH_CONTEXT_NO_CHUNKS